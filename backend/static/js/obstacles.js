const obstaclesArray = [];


class Obstacle {
    constructor(){
         this.position = (Math.random() * canvas.height);
         this.bottom = (Math.random()*canvas.height/3)+20;
         this.x = canvas.width;
         this.y = (Math.random() * canvas.height);
         this.width = 20;
         this.color = 'white';
         this.counted = false;
    }

    draw(){
        ctx.fillStyle = 'white';

        ctx.fillText("A",this.x-15, 60);
        ctx.fillText("B",this.x-15, 150);
        ctx.fillText("C",this.x-15, 250);
        ctx.fillText("D",this.x-15, 350);
        ctx.fillStyle = this.color;
        ctx.fillRect(this.x, 0, this.width, 95);
        ctx.fillRect(this.x, 100, this.width, 95);
        ctx.fillRect(this.x, 200, this.width, 95);
        ctx.fillRect(this.x, 300, this.width, 95);
        // ctx.arc(20,20,50,0,Math.PI*2);

        // ctx.fillRect(this.x, canvas.height - this.bottom, this.width, this.bottom);

    }
    update(){
        this.x -= gamespeed;
        this.draw();
    }
}


function handleObstacles(){
    if(frame%400 === 0){
        obstaclesArray.unshift(new Obstacle);
    }
    


    for (i = 0; i < obstaclesArray.length; i++) {
        obstaclesArray[i].update();
        
    }
    if(obstaclesArray.length > 4){
        obstaclesArray.pop(obstaclesArray[0]);
    }
}