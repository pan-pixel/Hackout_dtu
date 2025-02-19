const particlesArray = [];

class Particle{
    constructor(){
        this.x = rocket.x;
        this.y = rocket.y;
        this.size = Math.random()*2+2;
        this.speedY = (Math.random()*1) - 0.5;
        this.color = 'hsla('+hue+',100%, 50%, 0.8)';
    }

    update(){
        this.x -= gamespeed;
        this.y += this.speedY;
    }
    draw(){
        ctx.fillStyle = this.color;
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.size, 0, Math.PI*2);
        ctx.fill();
    }

}

function handleParticles(){
    particlesArray.unshift(new Particle);
    for (i = 0; i < particlesArray.length; i++) {
        particlesArray[i].update();
        particlesArray[i].draw();
        
    }
    if(particlesArray.length > 200){
        for (let i = 0; i < 20; i++) {
            particlesArray.pop(particlesArray[i]);
            
        }
    }
}