const headOne = document.querySelector("#one");
const headTwo = document.querySelector("#two");
const headThree = document.querySelector("#three");

headOne.addEventListener("mouseover", function(){
    headOne.textContent = "Mouse currently over";
    headOne.style.color = "red";
})

headOne.addEventListener("mouseout", function(){
    headOne.textContent = "Hover over me";
    headOne.style.color = "black";
})

headTwo.addEventListener("click", function(){
    headTwo.textContent = "Clicked!";
    headTwo.style.color = "green";
})

headThree.addEventListener("dblclick", function(){
    headThree.textContent = "Double click!";
    headThree.style.color = "green";
})