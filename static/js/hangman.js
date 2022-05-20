var letterElements = document.getElementsByClassName("letter_element");
var letterButtons = document.getElementsByClassName("letter_button");
var randomQuiz = "";
randomGenre = "";
randomQuiz = "";
var attempts = document.getElementsByClassName("attempt");
var unsuccessfulAttempts = 0;
var hangmanGrid = document.getElementById("hangman");
var glitchImg = document.getElementById("glitch_img");
var glitchLayers = document.getElementById("glitch_layers");
var title = document.getElementsByClassName("title")[0];
var glitchText = document.getElementsByClassName("glitch_text")[0];
var stage = document.getElementById("stage");
var currentStage = 1;
var stageCompletedText = document.getElementById("glitch_text_1");
var allCompletedElement = document.getElementById("glitch_text_2");
var allCompletedText = document.getElementById("glitch_text_content");
var randomIndex = 0;

const alpha = Array.from(Array(26)).map((e, i) => i + 65);
const alphabet = alpha.map((x) => String.fromCharCode(x));
for (let i = 0; i < letterButtons.length; i++) letterButtons[i].innerText = alphabet[i];

function newQuestion() {

    randomQuiz = quiz[Math.floor(Math.random() * quiz.length)];
    console.log(randomQuiz);
    console.log(quiz);
    randomIndex = quiz.indexOf(randomQuiz);
    randomGenre = randomQuiz["genre"];
    randomQuiz = randomQuiz["question"];
    quizTitle = document.getElementById("quiz_title");
    quizTitle.innerText = randomGenre;
    quizQuestion = document.getElementById("quiz_question");
    var questionContent = "";
    for (const letterButton of letterButtons) letterButton.classList.remove("tested");
    unsuccessfulAttempts = 0;
    for (let i = 0; i < randomQuiz.length; i++) {

        (RegExp(/^\p{L}/,'u').test(randomQuiz[i]))
        ? questionContent+= "_"
        : questionContent+= randomQuiz[i]

    }

    console.log(questionContent);

    quizQuestion.innerText = questionContent;
    console.log(quizQuestion.innerText.length);
    stage.innerText = `Current stage: ${currentStage}/10`;


}

newQuestion();

function checkLetter(event) {

    var letter = event.target.innerText;
    event.target.classList.add("tested");
    (randomQuiz.toUpperCase().includes(letter)) ? successfulAttempt(letter) : unsuccessfulAttempt(letter);
    if (quizQuestion.innerText == randomQuiz.toUpperCase()) { (currentStage == 10) ? allIsNowComplete() : questionCompleted() }

}

function unsuccessfulAttempt(letter) {

    unsuccessfulAttempts++;
    attempts[unsuccessfulAttempts - 1].style.color = "red";
    if (unsuccessfulAttempts == 4) questionFailed();

}

function successfulAttempt(letter) {

    for (let i = 0; i < randomQuiz.length; i++) if (letter == randomQuiz[i].toUpperCase()) { quizQuestion.innerText = quizQuestion.innerText.replaceAt(i, letter); }

}

async function questionCompleted() {

    hangmanGrid.style.display = "none";
    currentStage++;
    stageCompletedText.style.display = "block";
    quiz.splice(randomIndex, 1);
    console.log(quiz);
    await getGame(1200);
    hangmanGrid.style.display = "block";
    stageCompletedText.style.display = "none";
    for (const attempt of attempts) attempt.style.color = "inherit";
    newQuestion();

}

async function allIsNowComplete() {

    hangmanGrid.style.display = "none";
    currentStage++;
    allCompletedElement.style.display = "block";
    allCompletedText.innerText = "Congratulations!";
    await getGame(1360);
    allCompletedText.innerText = "Most people are so ungrateful to be alive...";
    await getGame(1360);
    allCompletedText.innerText = "But not you...";
    await getGame(1360);
    allCompletedText.innerText = "Not anymore...";
    await getGame(1200);

}

async function questionFailed() {

    hangmanGrid.style.display = "none";
    glitchImg.style.display = "block";
    glitchLayers.style.display = "block";
    title.style.display = "none";
    glitchText.style.display = "block";

}

String.prototype.replaceAt = function(index, replacement) {

    return this.substring(0, index) + replacement + this.substring(index + replacement.length);

}

function getGame(ms) {

    return new Promise(resolve => setTimeout(resolve, ms));

}

