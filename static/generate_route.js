const map = document.querySelector(".map");
const stations = document.querySelector(".stations")

for (let station of stations.children) {
    if(station.tagName == "LI") {
        console.log(station.textContent)
    }
}