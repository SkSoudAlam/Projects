const computerChoiceDisplay = document.getElementById("computer-choice")
const playerChoiceDislay = document.getElementById("player-choice")
const ResultDisplay = document.getElementById("result")
const possibleChoices = document.querySelectorAll('button');
let playerChoice;
let computerChoice
let result;


possibleChoices.forEach(possibleChoice => possibleChoice.addEventListener('click', (e) =>{
    playerChoice = e.target.id
    playerChoiceDislay.innerHTML = playerChoice
    generateComputerChoice();
    getResult();
}));


function generateComputerChoice() {
    const randomNumber = Math.floor(Math.random() * 3 +1
    )
    if (randomNumber === 1){
        computerChoice = 'Rock'
    }
    if (randomNumber === 3){
        computerChoice = 'Scissors'
    }
    if (randomNumber === 2){
        computerChoice = 'Paper'
    }
    computerChoiceDisplay.innerHTML = computerChoice
}

function getResult() {
    if (computerChoice === playerChoice) {
        result = 'its a draw!'
    }
    
    if (computerChoice === 'Rock' && playerChoice === 'Paper') {
        result = 'Player has won the game'
    }
    if (computerChoice === 'Scissors' && playerChoice === 'Rock') {
        result = 'Player won!'
    }
    if (computerChoice === 'Rock' && playerChoice === 'Scissors') {
        result = 'computer won'
    }
    if (computerChoice === 'Paper' && playerChoice === 'Scissors') {
        result = 'Player won'
    }
    if (computerChoice ==='Paper' && playerChoice ==="Rock") {
        result = 'Computer won'
    }
    if (computerChoice === 'Scissors' && playerChoice === 'paper') {
        result = "Player won!"
    }
    ResultDisplay.innerHTML = result
}

