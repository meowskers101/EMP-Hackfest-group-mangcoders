const express = require('express');
const ExcelJS = require('exceljs');
const cors = require('cors');
const bodyParser = require('body-parser');
const path = require('path');
const fs = require('fs');

const app = express();
const PORT = 3000;

// Middleware
app.use(cors());
app.use(bodyParser.json());
app.use(express.static(path.join(__dirname)));

// Path to the Excel file
const usersFilePath = path.join(__dirname, 'users.xlsx');

// Initialize Excel file if it doesn't exist
async function initializeExcelFile() {
    if (!fs.existsSync(usersFilePath)) {
        const workbook = new ExcelJS.Workbook();
        const worksheet = workbook.addWorksheet('Users');
        
        // Add headers
        worksheet.columns = [
            { header: 'Username', key: 'username', width: 20 },
            { header: 'Email', key: 'email', width: 30 },
            { header: 'Password', key: 'password', width: 30 },
            { header: 'Created Date', key: 'createdDate', width: 20 }
        ];
        
        await workbook.xlsx.writeFile(usersFilePath);
        console.log('Users Excel file created');
    }
}

// Function to read all users from Excel
async function readUsers() {
    const workbook = new ExcelJS.Workbook();
    await workbook.xlsx.readFile(usersFilePath);
    const worksheet = workbook.getWorksheet('Users');
    
    const users = [];
    worksheet.eachRow((row, rowNumber) => {
        if (rowNumber > 1) { // Skip header row
            users.push({
                username: row.getCell('username').value,
                email: row.getCell('email').value,
                password: row.getCell('password').value,
                createdDate: row.getCell('createdDate').value
            });
        }
    });
    
    return users;
}

// Function to add a new user to Excel
async function addUser(username, email, password) {
    const workbook = new ExcelJS.Workbook();
    await workbook.xlsx.readFile(usersFilePath);
    const worksheet = workbook.getWorksheet('Users');
    
    worksheet.addRow({
        username: username,
        email: email,
        password: password,
        createdDate: new Date().toLocaleString()
    });
    
    await workbook.xlsx.writeFile(usersFilePath);
}

// Signup endpoint
app.post('/api/signup', async (req, res) => {
    try {
        const { username, email, password, confirmPassword } = req.body;
        
        // Validate inputs
        if (!username || !email || !password || !confirmPassword) {
            return res.status(400).json({ success: false, message: 'All fields are required' });
        }
        
        if (password !== confirmPassword) {
            return res.status(400).json({ success: false, message: 'Passwords do not match' });
        }
        
        // Check if username already exists
        const users = await readUsers();
        const userExists = users.some(user => user.username.toLowerCase() === username.toLowerCase());
        
        if (userExists) {
            return res.status(400).json({ success: false, message: 'Username already exists' });
        }
        
        // Check if email already exists
        const emailExists = users.some(user => user.email.toLowerCase() === email.toLowerCase());
        
        if (emailExists) {
            return res.status(400).json({ success: false, message: 'Email already registered' });
        }
        
        // Add new user to Excel
        await addUser(username, email, password);
        
        res.json({ success: true, message: 'Account created successfully', username: username });
    } catch (error) {
        console.error('Signup error:', error);
        res.status(500).json({ success: false, message: 'Server error' });
    }
});

// Login endpoint
app.post('/api/login', async (req, res) => {
    try {
        const { email, password } = req.body;
        
        // Validate inputs
        if (!email || !password) {
            return res.status(400).json({ success: false, message: 'Email and password are required' });
        }
        
        // Check credentials against Excel
        const users = await readUsers();
        const user = users.find(u => u.email.toLowerCase() === email.toLowerCase());
        
        if (!user) {
            return res.status(401).json({ success: false, message: 'Invalid email or password' });
        }
        
        if (user.password !== password) {
            return res.status(401).json({ success: false, message: 'Invalid email or password' });
        }
        
        res.json({ success: true, message: 'Login successful', username: user.username });
    } catch (error) {
        console.error('Login error:', error);
        res.status(500).json({ success: false, message: 'Server error' });
    }
});

// Start server
app.listen(PORT, async () => {
    await initializeExcelFile();
    console.log(`Server running at http://localhost:${PORT}`);
});
