value = document.getElementById("exp_percentage").value;
expBarWidth = document.getElementById("exp_bar");
expBarWidth.style.width = `${value}%`;
expBarWidth.style.setProperty('--end-width', `${value}%`)
