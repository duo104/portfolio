const character = document.getElementById("character");
const block = document.getElementById("block");
const count_display = document.getElementById("count_html");


var count = 0;
count_display.innerHTML = "Score: " + count;
var characterTop = 
  parseInt(window.getComputedStyle(character).getPropertyValue("top"));
var blockLeft = 
  parseInt(window.getComputedStyle(block).getPropertyValue("left"));

function jump() {
  if (character.classList != "animate") {
    character.classList.add("animate");
    if (blockLeft<20 && blockLeft>0 && characterTop>=130) {
      return false;
    }
    count++;
    count_display.innerHTML = "Score: " + count;
    console.log(count);
  }
  setTimeout(function() {
    character.classList.remove("animate");
  }, 500);
}

var checkDead = setInterval(function() {
  var characterTop = 
  parseInt(window.getComputedStyle(character).getPropertyValue("top"));
  var blockLeft = 
  parseInt(window.getComputedStyle(block).getPropertyValue("left"));
  if (blockLeft<20 && blockLeft>0 && characterTop>=130) {
    block.style.animation = "none";
    block.style.display = "none";
    alert("u lose!");
  }
});

