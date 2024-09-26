const express = require('express');
const bodyParser = require('body-parser');
const mysql = require('mysql');
const path = require('path');

const app = express();
app.use(bodyParser.json());

// Serve static files (like your HTML, CSS, client-side JavaScript)
app.use(express.static(path.join(__dirname, 'public')));

// MySQL Connection
const db = mysql.createConnection({
    host: 'mysql-db', // Use the MySQL service name defined in docker-compose
    user: 'root',
    password: 'root',
    database: 'employeedb'
});

// Connect to MySQL
db.connect(err => {
    if (err) {
        console.error('Error connecting to MySQL:', err);
        return;
    }
    console.log('Connected to MySQL');
});

// Start Work Timer
app.post('/api/start', (req, res) => {
    const { employeeId, employeeName } = req.body;
    const startTime = new Date();
    
    // Check if the employee has already started work today
    const queryCheck = 'SELECT * FROM employees WHERE employee_id = ? AND date = CURDATE() AND start_time IS NOT NULL';
    
    db.query(queryCheck, [employeeId], (err, results) => {
        if (err) {
            return res.status(500).json({ message: 'Error checking work status' });
        }
        if (results.length > 0) {
            return res.status(400).json({ message: 'Work has already been started today' });
        }

        const query = 'INSERT INTO employees (employee_id, name, start_time, date) VALUES (?, ?, ?, CURDATE())';
        
        db.query(query, [employeeId, employeeName, startTime], (err, result) => {
            if (err) {
                return res.status(500).json({ message: 'Error saving data' });
            }
            res.status(200).json({ message: 'Work started successfully', id: result.insertId });
        });
    });
});

// End Work Timer
app.post('/api/end', (req, res) => {
    const { employeeId } = req.body;
    const endTime = new Date();
    
    // Check if the employee has already ended work today
    const queryCheck = 'SELECT * FROM employees WHERE employee_id = ? AND date = CURDATE() AND end_time IS NOT NULL';
    
    db.query(queryCheck, [employeeId], (err, results) => {
        if (err) {
            return res.status(500).json({ message: 'Error checking work status' });
        }
        if (results.length > 0) {
            return res.status(400).json({ message: 'Work has already been ended today' });
        }

        const query = 'UPDATE employees SET end_time = ? WHERE employee_id = ? AND date = CURDATE() AND start_time IS NOT NULL';
        
        db.query(query, [endTime, employeeId], (err, result) => {
            if (err) {
                return res.status(500).json({ message: 'Error updating data' });
            }
            res.status(200).json({ message: 'Work timer ended successfully' });
        });
    });
});

// Save Break Times
app.post('/api/break/start', (req, res) => {
    const { employeeId } = req.body;
    const breakStart = new Date();

    // Check if the employee has started work
    const queryCheckWork = 'SELECT start_time FROM employees WHERE employee_id = ? AND date = CURDATE() AND start_time IS NOT NULL';
    
    db.query(queryCheckWork, [employeeId], (err, results) => {
        if (err || results.length === 0) {
            return res.status(400).json({ message: 'You need to start work before taking a break.' });
        }

        // Check if a break has already been taken today
        const queryCheckBreak = 'SELECT break_start FROM employees WHERE employee_id = ? AND date = CURDATE() AND break_start IS NOT NULL';
        
        db.query(queryCheckBreak, [employeeId], (err, results) => {
            if (err) {
                return res.status(500).json({ message: 'Error checking break status' });
            }
            if (results.length > 0) {
                return res.status(400).json({ message: 'You can only take one break per day.' });
            }

            const query = 'UPDATE employees SET break_start = ? WHERE employee_id = ? AND date = CURDATE() AND start_time IS NOT NULL';
            
            db.query(query, [breakStart, employeeId], (err, result) => {
                if (err) {
                    return res.status(500).json({ message: 'Error saving break start time' });
                }
                res.status(200).json({ message: 'Break started successfully' });
            });
        });
    });
});

app.post('/api/break/end', (req, res) => {
    const { employeeId } = req.body;
    const breakEnd = new Date();

    const query = 'UPDATE employees SET break_end = ? WHERE employee_id = ? AND date = CURDATE() AND break_start IS NOT NULL';

    db.query(query, [breakEnd, employeeId], (err, result) => {
        if (err) {
            return res.status(500).json({ message: 'Error saving break end time' });
        }
        res.status(200).json({ message: 'Break ended successfully' });
    });
});

// Fetch Employee Records (optional)
app.get('/api/employee/:id', (req, res) => {
    const employeeId = req.params.id;
    const query = 'SELECT * FROM employees WHERE employee_id = ? AND date = CURDATE()';

    db.query(query, [employeeId], (err, results) => {
        if (err) {
            return res.status(500).json({ message: 'Error fetching records' });
        }
        res.json(results);
    });
});

// Start the server
app.listen(5000, () => {
    console.log('Server running on port 5000');
});

