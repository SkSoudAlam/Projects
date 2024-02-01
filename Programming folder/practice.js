// practice.js

document.addEventListener('DOMContentLoaded', function() {
    let radius = document.getElementById('radius');
    let circumferenceButton = document.getElementById('circumference');
    let diameterButton = document.getElementById('diameter');
    let areaButton = document.getElementById('area');

    circumferenceButton.addEventListener('click', function() {
        let radius1 = parseFloat(radius.value);
        alert(radius1 * 6.28);
    });

    diameterButton.addEventListener('click', function() {
        let radius2 = parseFloat(radius.value);
        alert(radius2 * 2);
    });

    areaButton.addEventListener('click', function() {
        let radius3 = parseFloat(radius.value);
        alert(radius3 * radius3 * 3.14);
    });
});
