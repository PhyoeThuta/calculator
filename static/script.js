// Store calculation history
let history = [];

/**
 * Perform a calculation by calling the backend API
 * @param {string} operation - The operation to perform (add, subtract, multiply, divide)
 */
function calculate(operation) {
    // Get input values
    const num1 = parseFloat(document.getElementById('num1').value);
    const num2 = parseFloat(document.getElementById('num2').value);
    
    // Get error and result elements
    const errorDiv = document.getElementById('error');
    const resultDiv = document.getElementById('result');
    
    // Validate inputs
    if (isNaN(num1) || isNaN(num2)) {
        showError('Please enter valid numbers');
        resultDiv.classList.remove('show');
        return;
    }
    
    // Clear previous error
    hideError();
    
    // Make API call to backend
    const url = `/${operation}?a=${num1}&b=${num2}`;
    
    fetch(url)
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                showError(data.error);
                resultDiv.classList.remove('show');
            } else {
                // Display result
                const result = data.result;
                document.getElementById('resultValue').textContent = result;
                resultDiv.classList.add('show');
                
                // Add to history
                addToHistory(num1, operation, num2, result);
                
                // Clear inputs for next calculation
                document.getElementById('num1').value = '';
                document.getElementById('num2').value = '';
                document.getElementById('num1').focus();
            }
        })
        .catch(error => {
            showError('Error: Unable to connect to server');
            console.error('Fetch error:', error);
        });
}

/**
 * Add a calculation to the history list
 * @param {number} num1 - First number
 * @param {string} operation - Operation performed
 * @param {number} num2 - Second number
 * @param {number} result - Result of calculation
 */
function addToHistory(num1, operation, num2, result) {
    // Create history entry
    const entry = `${num1} ${getOperationSymbol(operation)} ${num2} = ${result}`;
    history.unshift(entry); // Add to beginning
    
    // Keep only last 10 calculations
    if (history.length > 10) {
        history.pop();
    }
    
    // Update history display
    updateHistoryDisplay();
}

/**
 * Get the symbol for an operation
 * @param {string} operation - The operation name
 * @returns {string} The symbol for the operation
 */
function getOperationSymbol(operation) {
    const symbols = {
        'add': '+',
        'subtract': '-',
        'multiply': '×',
        'divide': '÷'
    };
    return symbols[operation] || operation;
}

/**
 * Update the history display on the page
 */
function updateHistoryDisplay() {
    const historyList = document.getElementById('historyList');
    
    if (history.length === 0) {
        historyList.innerHTML = '<li>No calculations yet</li>';
        return;
    }
    
    historyList.innerHTML = history
        .map(entry => `<li>${entry}</li>`)
        .join('');
}

/**
 * Show error message
 * @param {string} message - Error message to display
 */
function showError(message) {
    const errorDiv = document.getElementById('error');
    errorDiv.textContent = `Error: ${message}`;
    errorDiv.classList.add('show');
}

/**
 * Hide error message
 */
function hideError() {
    const errorDiv = document.getElementById('error');
    errorDiv.classList.remove('show');
}

/**
 * Handle Enter key press for quick calculation
 */
document.addEventListener('DOMContentLoaded', function() {
    const inputs = document.querySelectorAll('input[type="number"]');
    
    inputs.forEach(input => {
        input.addEventListener('keypress', function(event) {
            if (event.key === 'Enter') {
                calculate('add'); // Default to add on Enter
            }
        });
    });
    
    // Focus on first input
    document.getElementById('num1').focus();
});
