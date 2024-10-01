let transactions = [];
const balanceElement = document.getElementById('account-balance');
const transactionsListElement = document.getElementById('transactions-list');
const transactionForm = document.getElementById('transaction-form');

// Function to calculate and update account balance
function updateBalance() {
    const balance = transactions.reduce((acc, transaction) => acc + transaction.amount, 0);
    balanceElement.textContent = balance.toFixed(2);
}

// Function to render transactions list
function renderTransactions() {
    transactionsListElement.innerHTML = '';

    if (transactions.length === 0) {
        transactionsListElement.innerHTML = '<p>No transactions yet.</p>';
        return;
    }

    transactions.forEach((transaction) => {
        const transactionItem = document.createElement('div');
        transactionItem.classList.add('transaction');
        // Add a console log to inspect transaction structure
        console.log('Rendering transaction:', transaction);
        transactionItem.innerHTML = `
            <p>${transaction.date} - ${transaction.description} (${transaction.type}): R${transaction.amount.toFixed(2)}</p>
            <button onclick="deleteTransaction('${transaction.id}')">Delete</button>
        `;
        transactionsListElement.appendChild(transactionItem);
    });
}

// Function to delete a transaction
async function deleteTransaction(id) {
    await fetch(`http://localhost:4999/transactions/${id}`, {
        method: 'DELETE'
    });
    fetchTransactions(); // Refresh the transaction list after deletion
}

// Function to fetch transactions from the API
async function fetchTransactions() {
    try {
        const response = await fetch('http://localhost:4999/transactions/', {
            method: 'GET',  // Change to GET for fetching data
            headers: {
                'Content-Type': 'application/json'
            },
            mode: 'cors'  // This is important for cross-origin requests
        });

        if (!response.ok) throw new Error('Failed to fetch transactions');

        transactions = await response.json();
        // Ensure each transaction has an amount defined
        transactions.forEach(transaction => {
            transaction.amount = parseFloat(transaction.amount); // Ensure amount is a number
        });
        renderTransactions();
        updateBalance();
    } catch (error) {
        console.error('Error fetching transactions:', error);
    }
}

// Event listener for adding a new transaction
transactionForm.addEventListener('submit', async function (e) {
    e.preventDefault();

    const type = document.getElementById('type').value;
    const description = document.getElementById('description').value;
    const date = document.getElementById('date').value;
    const amount = parseFloat(document.getElementById('amount').value);

    if (date && description && !isNaN(amount)) {
        const transaction = {
            type,
            description,
            date,
            amount: type === 'debit' ? -amount : amount
        };

        // Send the new transaction to the API
        try {
            const response = await fetch('http://localhost:4999/transactions/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(transaction)
            });

            if (!response.ok) throw new Error('Failed to add transaction');

            // After adding, fetch the updated list of transactions
            fetchTransactions();
            transactionForm.reset(); // Clear the form
        } catch (error) {
            console.error('Error adding transaction:', error);
        }
    }
});

// Initial fetch of transactions
fetchTransactions();
