// datos
function consumir_api() {
    let api_char = "http://127.0.0.1:5000/API"

    fetch(api_char)
        .then((response) => response.json())
        .then((data) => {
            genchart(data);
        });
}

function genchart(data) {
    const test = {
        labels: ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes'], //Etiquetas que aparecen en la barritas
        datasets: [{ //valores
            label: 'Entradas', //nombre de la barrita de arriba
            data: [10, 12, 6, 9, 12, 3, 9], //Porcentaje de la barrita
            backgroundColor: [
                'rgba(144, 238, 144, 0.5)',
            ],
            borderColor: [
                'rgba(144, 238, 144, 3)',
            ],
            borderWidth: 1
        },
        { //valores
            label: 'Salidas', //nombre de la barrita de arriba
            data: [2, 12, 6, 9, 12, 3, 9], //Porcentaje de la barrita
            backgroundColor: [
                'rgba(0, 250, 154, 0.3)',
            ],
            borderColor: [
                'rgba(0, 128, 128, 0.3)',
            ],
            borderWidth: 1
        }]
    };




    // config 
    const config = {
        type: 'bar',
        test,
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    };

    // render init block
    const myChart = new Chart(
        document.getElementById('reportes'), //Aqui se pone el nobre que se puso en el id del html 
        config
    );

}
