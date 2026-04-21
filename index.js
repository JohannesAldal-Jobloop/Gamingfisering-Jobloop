let expFyllElement = document.getElementById("expFyll");
let expBarElement = document.getElementById("expBar");
let levelTellerElement = document.getElementById("levelTeller")
let exp = 0;
let level = 0;

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

function levering() {
    exp += 10;
    expFyllElement.style.width = (exp.toString() + "%");

    if(exp >= 94){
        level++;
        levelTellerElement.innerHTML = level;
        expFyllElement.style.width = "94%";
        expFyllElement.style.borderColor = "red";

        expBarElement.style.animationName = "levelOpp";

        setTimeout(() => {
            exp = 0;
            expFyllElement.style.width = (exp.toString() + "%");
            expFyllElement.style.borderColor = "orange";
            expBarElement.style.animationName = "";
        }, 3000)
        
    };
}