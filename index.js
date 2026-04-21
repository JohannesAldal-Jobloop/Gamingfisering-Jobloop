let expFyllElement = document.getElementById("expFyll");
let levelTellerElement = document.getElementById("levelTeller")
let exp = 0;
let level = 0;

function levering() {
    exp += 10;
    expFyllElement.style.width = (exp.toString() + "%");

    if(exp >= 94){
        level++;
        levelTellerElement.innerHTML = level;
        expFyllElement.style.width = "94%";
        expFyllElement.style.borderColor = "red";
        exp = 0;
        expFyllElement.style.width = (exp.toString() + "%");
    };
}