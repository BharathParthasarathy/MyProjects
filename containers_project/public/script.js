// Start Work
async function startWork() {
    const employeeId = document.getElementById('employeeId').value;
    const employeeName = document.getElementById('employeeName').value;

    try {
        const response = await fetch('/api/start', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ employeeId, employeeName }),
        });

        const data = await response.json();
        alert(data.message); // Show success or error message
    } catch (error) {
        console.error('Error starting work:', error);
        alert('Error starting work, please try again.');
    }
}

// End Work
async function endWork() {
    const employeeId = document.getElementById('employeeId').value;

    try {
        const response = await fetch('/api/end', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ employeeId }),
        });

        const data = await response.json();
        alert(data.message); // Show success or error message
    } catch (error) {
        console.error('Error ending work:', error);
        alert('Error ending work, please try again.');
    }
}

// Start Break
async function startBreak() {
    const employeeId = document.getElementById('employeeId').value;

    try {
        const response = await fetch('/api/break/start', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ employeeId }),
        });

        const data = await response.json();
        alert(data.message); // Show success or error message
    } catch (error) {
        console.error('Error starting break:', error);
        alert('Error starting break, please try again.');
    }
}

// End Break
async function endBreak() {
    const employeeId = document.getElementById('employeeId').value;

    try {
        const response = await fetch('/api/break/end', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ employeeId }),
        });

        const data = await response.json();
        alert(data.message); // Show success or error message
    } catch (error) {
        console.error('Error ending break:', error);
        alert('Error ending break, please try again.');
    }
}

// Event listeners for buttons
document.getElementById('startWork').addEventListener('click', startWork);
document.getElementById('endWork').addEventListener('click', endWork);
document.getElementById('startBreak').addEventListener('click', startBreak);
document.getElementById('endBreak').addEventListener('click', endBreak);

