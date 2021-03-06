'use strict';

{
  const target = document.getElementById('target');
  const scoreLabel = document.getElementById('score');
  const missLabel = document.getElementById('miss');
  const timerLabel = document.getElementById('timer');

  const words = [
    'apple',
    'sky',
    'blue',
    'middle',
    'set',
    'what',
    'the',
    'end',
    'enter',
    'door',
    'miracle',
    'element',
  ];
  let word = words[Math.floor(Math.random() * words.length)];
  let loc = 0;
  let score = 0;
  let miss = 0;
  let startTime;
  const timeLimit = 3 * 1000;
  let isPlaying = false;

  function updateTarget() {
    let placeholder = '';
    for (let i = 0; i < loc; i++) {
      placeholder += '_';
    }
    target.textContent = placeholder + word.substring(loc);
  }

  function updateTimer() {
    const leftTime = startTime + timeLimit - Date.now();
    timerLabel.textContent = (leftTime / 1000).toFixed(2);

    const timeoutId = setTimeout( () => {
      updateTimer();
    }, 10);

    if (timeLeft < 0) {
      clearTimeout(timeoutId);
      timerLabel.textContent = '0.00';
      setTimeout(() => {
        alert('Game Over');
      }, 100);
    }
  }

  window.addEventListener('click', () => {
    if (isPlaying) {
      return;
    }
    
    isPlaying = true;
    target.textContent = word;
    startTime = Date.now();
    updateTimer();
  });

  window.addEventListener('keydown', e => {
    console.log(e.key);
    if (e.key === word[loc]) {
      loc++;
      if (loc === word.length) {
        word = words[Math.floor(Math.random() * words.length)];
        loc = 0;
      }
      score++;
      scoreLabel.textContent = score;
      updateTarget();
    } else {
      miss++;
      missLabel.textContent = miss;
    }
  });
  
  
}