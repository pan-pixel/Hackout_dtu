const RocketSprite = new Image()
RocketSprite.src = "rocket.png";

class Rocket{
    constructor(){
        this.x = 150;
        this.y = 200;
        this.vy = 0;
        this.originalheight = 1037;
        this.originalwidth = 482;
        this.width = 45;
        // this.width = this.originalwidth/40;
        this.height = 25;
        // this.height = this.originalheight/40;

        this.weight = 1;
    }

    update(){ 
        let curve = Math.sin(angle) * 10;
        if(this.y > canvas.height - (this.height*2) + curve){
            this.y = canvas.height - (this.height*2) + curve;
            this.vy = 0;
        }
        else{
            this.vy += this.weight;
            this.vy *= 0.8;
            this.y += this.vy;
        }
        if(this.y < 0 +this.height){
            this.y = 0 + this.height;
            this.vy = 0;
        }
        if(spacePressed && this.y > this.height * 2){
            this.flap();
        }
        
    }

    draw(){
        ctx.fillStyle = 'white';
        ctx.fillRect(this.x, this.y, this.width, this.height);
        // ctx.arc(50,50,50,0,Math.PI*2);


        // ctx.drawImage(RocketSprite,0,0,this.originalwidth,this.originalheight,this.x,this.y,this.width*2,this.height*2);

    }
    flap(){
        this.vy -= 2;
    }



}

const rocket = new Rocket();