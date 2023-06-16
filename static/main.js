const mapa = document.querySelector(".map");
const formStation = document.querySelector(".form-station");
const loadingScreen = document.querySelector(".loading");
const estaciones = document.querySelectorAll(".station");
const startStation = document.querySelector("#start");
const endStation = document.querySelector("#end");
const colorRojo = 'rgb(217, 38, 26)';
const colorNaranja = 'rgb(238, 149, 58)';
const colorAmarillo = 'rgb(250, 195, 3)';
const colorAzulClaro = 'rgb(150, 207, 184)';
const colorOlivo = 'rgb(158, 154, 58)';
const colorAzul = 'rgb(1, 124, 192)';
const colorVerde = 'rgb(3, 146, 63)';
const colorGris = 'rgb(169, 169, 169)';
const colorRosa = 'rgb(211, 85, 144)';
const colorCafe = 'rgb(141, 85, 68)';

let startSelected = undefined;
let endSelected = undefined;
let start = true;

function drawLine(X1, X2, color) {
    const x1 = X1[0];
    const y1 = X1[1];
    const x2 = X2[0];
    const y2 = X2[1];

    const xm = (x1 + x2 / 2);
    const ym = (y1 + y2 / 2);
    const lineLength = Math.sqrt((x1 - x2)**2 + (y1 - y2)**2);
    let slope = 0;

    if(x1 === x2) slope = 90
    else if (y1 === y2) slope = 00
    else slope = Math.atan((y2 - y1)/(x2 - x1)) * 180 / Math.PI;

    const newLine = document.createElement("div");
    newLine.className = "line";
    newLine.style.backgroundColor = color;
    newLine.style.transform = `rotate(${slope}deg)`;
    newLine.style.width = `${lineLength}px`;
    newLine.style.left = `${x1 + 5}px`;
    newLine.style.top = `${y1 + 5}px`;

    mapa.appendChild(newLine);
}

for(station of estaciones) {
    station.addEventListener('click', event => {
        element = event.target;
        elementClass = element.className;
        parent = element.parentElement;
        stationNode = parent.children[0];
        currentStation = parent.children[1].textContent;

        if(start) {
            if (startSelected) {
                startSelected.style.backgroundColor = "white";
                startSelected.parentElement.style.color = "black";
            }
            startStation.value = currentStation;
            startSelected = stationNode;
            startSelected.style.backgroundColor = "#3FA242"
            startSelected.parentElement.style.color  = "#3FA242";
        } else {
            if (endSelected) {
                endSelected.style.backgroundColor = "white";
                endSelected.parentElement.style.color = "black"
            }
            endSelected = stationNode;
            endStation.value = currentStation;
            endSelected.style.backgroundColor = "#D94745";
            endSelected.parentElement.style.color = "#D94745";
        }

        start = !start;
    })
}

formStation.addEventListener('submit', event => {
    loadingScreen.style.display = "block"
})


// Linea roja
drawLine([471, 166], [600, 166], colorRojo)
drawLine([187, 114], [471, 166], colorRojo)
drawLine([471, 166], [839, 166], colorRojo)

// Linea naranja
drawLine([187, 114], [187, 334], colorNaranja)
drawLine([187, 334], [187, 744], colorNaranja)

// Linea amarilla
drawLine([471, 166], [547, 242], colorAmarillo);
drawLine([547, 242], [839, 301],colorAmarillo);
drawLine([839, 301], [1019, 404], colorAmarillo);
drawLine([1019, 404], [1095, 694], colorAmarillo);

// Linea azul claro
drawLine([839, 166], [839, 301], colorAzulClaro);
drawLine([839, 301], [839, 415], colorAzulClaro);
drawLine([839, 415], [839, 462], colorAzulClaro);
drawLine([839, 462], [839, 744], colorAzulClaro);
drawLine([839, 744], [839, 813], colorAzulClaro);

// Linea verde olivo
drawLine([547,242], [600, 166],colorOlivo);
drawLine([470,376], [547,242],colorOlivo);
drawLine([470,376], [470,321],colorOlivo);
drawLine([470,421], [470, 575],colorOlivo);
drawLine([470, 575], [470, 744], colorOlivo);

// Linea Azul
drawLine([187,334], [470, 421], colorAzul);
drawLine([470, 421], [570, 421], colorAzul);
drawLine([570, 421], [698, 575], colorAzul);
drawLine([698, 575], [698, 744], colorAzul);

// Linea Verde
drawLine([570, 376], [570, 421], colorVerde);
drawLine([570, 421], [570, 575], colorVerde);
drawLine([570, 575], [698, 744], colorVerde);
drawLine([698, 744], [839, 813], colorVerde);

// Linea Gris
drawLine([470, 376], [570, 376], colorGris);
drawLine([570, 376], [839, 415], colorGris);
drawLine([839, 415], [886, 460], colorGris);
drawLine([886, 460], [1019, 404], colorGris);

// Linea Rosa
drawLine([187, 744], [470, 575], colorRosa);
drawLine([470, 575], [570, 575], colorRosa);
drawLine([570, 575], [698, 575], colorRosa);
drawLine([698, 575], [839, 462], colorRosa);
drawLine([839, 462], [886, 460], colorRosa);
drawLine([886, 460], [1095, 694], colorRosa);

// Linea cafe
drawLine([187, 744], [470, 744], colorCafe);
drawLine([470, 744], [698, 744], colorCafe);
drawLine([698, 744], [839, 744], colorCafe);
drawLine([839, 744], [1095, 694], colorCafe);