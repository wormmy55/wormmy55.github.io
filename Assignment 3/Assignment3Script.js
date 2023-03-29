/*
      Author: Jonathan Au - 300827701
      Date:   2023/03/29

      Filename: Assignment3.html
*/


const gameSpeedDisplay = document.getElementById("GameSpeed");
const reset_score = document.getElementById("resetScoreBtn");
const reset_speed = document.getElementById("resetSpeedBtn");
const scoreEl = document.getElementById("ScoreBoard");

let field = document.getElementById("mainBack");
let bugEl = document.createElement("div");
//let fieldContext = field.getContext("2d");
//bugEl.offsetWidth = 80 + "px";
//bugEl.offsetHeight = 80 + "px";
//document.body.appendChild(field);
let time = 10000;
let moveTimer = time;   //time until the picture moves in 'ms'
let levelCounter = 10;  //changes depending on the level
let speedCounter = 10;  //waypoint to determint when to increment
let gameSpeed = 1.0;    //speed multiplier
let ScoreBoard = 0;     //scoreboard
let toggleState = 0;

bugEl.id = "target";
/*
bugEl.addEventListener(onload, ()=>{
    caughtBug();
    renderBug();
})*/
bugEl.addEventListener("onload", ()=>{
    caughtBug();
    renderBug();
})


scoreEl.innerHTML = "Score: " + ScoreBoard;
gameSpeedDisplay.innerHTML = "Speed: " + gameSpeed.toFixed(2) + "x";

//add point to scoreboard
bugEl.addEventListener("click", ()=>{
    ScoreBoard ++;
    scoreEl.innerHTML = "Score: " + ScoreBoard;
    SPDincrease();
    caughtBug();
    renderBug();
});

bugEl.addEventListener(timer(), ()=>{
    caughtBug();
    renderBug();
})

//reset score
reset_score.addEventListener("click", ()=> {
    ScoreBoard = 0;
    speedCounter = 10;
    scoreEl.innerHTML = "Score: " + ScoreBoard;
});

//reset speed
reset_speed.addEventListener("click", ()=> {
    gameSpeed = 1.00;
    speedCounter = ScoreBoard + levelCounter;
    moveTimer = time;
    gameSpeedDisplay.innerHTML = "Speed: " + gameSpeed.toFixed(2) + "x";
    console.log("speed has been reset");
});

function increments() {
    speedCounter = speedCounter + levelCounter;
    moveTimer = moveTimer / gameSpeed;
};

function SPDincrease() {
    if (ScoreBoard <= 50 && ScoreBoard == speedCounter) {
        levelCounter = 10;
        gameSpeed = gameSpeed + 0.1;
        gameSpeedDisplay.innerHTML = "Speed: " + gameSpeed.toFixed(2) + "x";
        field.style.backgroundImage = "url('Images/background1.png')";
        increments();
        console.log(moveTimer);
        console.log("increase speed");
    } else if (ScoreBoard <= 100 && ScoreBoard == speedCounter) {
        levelCounter = 5;
        gameSpeed = gameSpeed + 0.5;
        gameSpeedDisplay.innerHTML = "Speed: " + gameSpeed.toFixed(2) + "x";
        field.style.backgroundImage = "url('Images/background3.jpg')";
        increments();
        console.log("increase speed level 2");
    }else if (ScoreBoard <= 150 && ScoreBoard == speedCounter) {
        levelCounter = 2;
        gameSpeed = gameSpeed + 2.5;
        gameSpeedDisplay.innerHTML = "Speed: " + gameSpeed.toFixed(2) + "x";
        field.style.backgroundImage = "url('Images/background1.png')";
        increments();
        console.log("increase speed level 3");
    }else if (ScoreBoard > 150 && ScoreBoard == speedCounter) {
        levelCounter = 1;
        gameSpeed = gameSpeed + 5.0;
        gameSpeedDisplay.innerHTML = "Speed: " + gameSpeed.toFixed(2) + "x";
        field.style.backgroundImage = "url('Images/background3.jpg')";
        increments();
        console.log("increase speed level 4");
    }
};

function timer() {
    if (moveTimer > 0) {
        setTimeout(timer, moveTimer);
        caughtBug();
        renderBug();
        //console.log(moveTimer);
        return;
    }
}

function renderBug() {
    field.appendChild(bugEl);
}

//randomize bug location
function caughtBug() {
    //let bugElWidth = bugEl.offsetWidth;
    //let bugElHeight = bugEl.offsetHeight;
    let fieldWidth = field.offsetWidth - 80;
    let fieldHeight = field.offsetHeight - 80;
    //bugEl.style.left = (Math.random() * (fieldWidth) + "px");
    //bugEl.style.top = (Math.random() * (fieldHeight) + "px");

    //console.log(math.random());
    //console.log(bugElWidth);
    //console.log(bugElHeight);
    //console.log(field.offsetWidth);
    //console.log(field.offsetHeight);
    //bugEl.style.top = 10 +"px";
    //bugEl.style.left = 15 + "px";

    let randomTop = getRandomNumber(0, fieldHeight);
    let randomLeft = getRandomNumber(0, fieldWidth);
    bugEl.style.top = randomTop + 1 + "px";
    bugEl.style.left = randomLeft + 1 + "px";
};


// function that returns a random number between a min and max
function getRandomNumber(min, max) {
    
  return Math.random() * (max - min) -min;
    
};

function toggle() {
    var element = document.body;
    element.classList.toggle("dark-mode");
    let darkBtn = document.getElementById("darkMode");
    if (toggleState == 0) {
        darkBtn.innerHTML = "Let there be light!";
        toggleState = 1;
        console.log(to)
    } else if (toggleState == 1) {
        darkBtn.innerHTML = "Too Bright!";
        toggleState = 0;
    }
}

//note: make this reuseable
/*
let intervalId = setInterval(function() {
    console.log('bug will move');
});

function stop(){
    clearInterval(intervalId);
};
*/
//to do 1 - window onload -- to start moving bug initially
//to do 2 - use canvase for the background and for jumping logic
// have bug flash element x game
//to do 3 - set interval to different speed
