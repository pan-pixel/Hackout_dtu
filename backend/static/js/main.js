const canvas = document.getElementById('canvas1');
const ctx = canvas.getContext('2d');
canvas.width = 600;
canvas.height = 400;
// canvas.
const questions = ["What is a mutual fund?",
"Who manages the investments in a mutual fund?",
"Which of the following is NOT a type of mutual fund?",
"What is the primary advantage of investing in mutual funds?",
"What is Net Asset Value (NAV) in the context of mutual funds?",
"Which regulatory body oversees mutual funds in the United States?",
"What is an expense ratio in mutual funds?",
"What is a load in mutual funds?",
"Which type of mutual fund typically aims to match the performance of a specific market index?",
"What is dollar-cost averaging in mutual fund investing?"];

const options = [
    ["a) An individual stock investment", "b) A type of savings account", "c) An investment vehicle that pools money from multiple investors to invest in a diversified portfolio of assets", "d) A government bond"],
    ["a) Individual investors", "b) The government", "c) Professional fund managers", "d) Financial advisors"],
    ["a) Equity fund", "b) Index fund", "c) Real estate fund", "d) Treasury bond fund"],
    ["a) Guaranteed returns", "b) High liquidity", "c) Diversification", "d) Tax deductions"],
    ["a) The total value of assets held by the fund minus liabilities, divided by the number of outstanding shares", "b) The amount of money a mutual fund manager earns", "c) The initial investment required to buy into a mutual fund", "d) The percentage of profits distributed to shareholders"],
    ["a) Federal Reserve", "b) Securities and Exchange Commission (SEC)", "c) Department of the Treasury", "d) Federal Deposit Insurance Corporation (FDIC)"],
    ["a) The percentage of assets deducted annually to cover fund expenses", "b) The interest rate applied to borrowings by the mutual fund", "c) The commission paid to the fund manager", "d) The fee charged for selling shares of the mutual fund"],
    ["a) The fee charged by the fund manager for purchasing shares", "b) The process of selling shares in a mutual fund", "c) The total value of assets held by the mutual fund", "d) The distribution of profits to shareholders"],
    ["a) Hedge fund", "b) Growth fund", "c) Index fund", "d) Balanced fund"],
    ["a) Investing a fixed amount of money at regular intervals, regardless of market conditions", "b) Investing a variable amount of money based on market fluctuations", "c) Buying mutual fund shares only when the market is at its peak", "d) Selling mutual fund shares when the market is experiencing a downturn"]
];

const answers = ["c", "c", "d", "c", "a", "b", "a", "a", "c", "a"];

let ch;

let inc = 0;
let spacePressed = false;
let angle = 0;
let hue = 0;
let frame = 0;
let score = 0;
let gamespeed = 2;
let ans = 0;
let isChangeques = false;

// temp = canvas.height - 90;

function animate(){
    ctx.clearRect(0,0,canvas.width, canvas.height);
    ctx.fillText("Score: "+score,canvas.width - 80, 390 );
    // ctx.fillRect(10,canvas.height - 90,50,20);
    handleObstacles();
    handleParticles();
    console.log(ans);
    rocket.update();
    rocket.draw();
    handleCollisions(ans);
    generateQuestion();
    if(handleCollisions()) return;
    requestAnimationFrame(animate);
    angle+=0.1;
    if(hue>=60){
        hue = 0;
    }
    hue++;
    frame++;
}

animate();


window.addEventListener('keydown', function(e){
    if(e.code === 'Space') spacePressed = true;
 
});

window.addEventListener('keyup',function(e){
    if(e.code === 'Space') spacePressed = false;
})

function generateQuestion(){
    ctx.fillStyle = 'white';

    ctx.font = '15px arial';
    ctx.fillText(questions[inc],20,15);
    for(i=0;i<=3;i++){
        ctx.fillText(options[inc][i],20,30 + (i*15));
    }
}



function handleCollisions(){
    for (let i = 0; i < obstaclesArray.length; i++) {
        if(rocket.x< obstaclesArray[i].x + obstaclesArray[i].width && rocket.x + rocket.width > obstaclesArray[i].x){
            if(!obstaclesArray[i].counted){
                obstaclesArray[i].counted = true;
                inc++;
                if(rocket.y >0 && rocket.y < 100){
                    ch = 'a'
                    console.log(1);
                }
                else if(rocket.y>100 && rocket.y<200){
                    ch = 'b'
                    console.log(2);

                }
                else if(rocket.y >200 && rocket.y < 300){
                    ch = 'c'
                    console.log(3);

                }
                else{
                    ch = 'd'
                    console.log(4);

                }
                if(ch == answers[inc]){
                    score+=10;
                }
                else{
                    score -= 5;
                }
                

            }
        }
    }
}