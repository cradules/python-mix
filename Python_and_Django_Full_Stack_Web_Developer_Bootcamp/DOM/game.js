//get button

const restart = document.querySelector('#restart_b');

// Grab all squares

const squares = document.querySelectorAll('td');

for (let i = 0; i < squares.length; i++) {
    squares[i].textContent = '';
}

// Clear Squares Function
restart.addEventListener('click', function () {
    for (let i = 0; i < squares.length; i++) {
        squares[i].textContent = '';
    }
})

function changeMarker() {
    if (this.textContent === '') {
        this.textContent = 'X';
    } else if (this.textContent === 'X') {
        this.textContent = 'O';
    } else {
        this.textContent = '';
    }
}

// Use a for loop to add Event listeners to all the squares
for (let i = 0; i < squares.length; i++) {
    squares[i].addEventListener('click', changeMarker);
}