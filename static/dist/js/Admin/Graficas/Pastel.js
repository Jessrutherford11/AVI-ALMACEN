
        function consumir_api() {
          let api_char = "http://127.0.0.1:5000/API"

          fetch(api_char)
            .then((response) => response.json())
            .then((data) => {
              genchart(data);
            });
        }

        function genchart(data) {
          const ctx = document.getElementById("Pastel");

          new Chart(ctx, {
            type: "bar",
            data: {
              labels:['Lunes', 
              'Martes', 
              'Miercoles', 
              'Jueves', 
              'Viernes'], 
              datasets: [
                {
                  label: "Entradas",
                  data: [
                    data.entradas,
                    data.entradas,
                    data.salidas,
                    data.salidas,
                    data.entradas,
                  ],
                  backgroundColor: [
                    'rgba(144, 238, 144, 0.5)',
                  ],
                  borderColor: [
                    'rgba(144, 238, 144, 3)',
                ],
                borderWidth: 1,
                },
                { //valores
                  label: 'Salidas', //nombre de la barrita de arriba
                  data:[ data.salidas, 
                  data.salidas, //Porcentaje de la barrita
                  ],
                  backgroundColor: [
                      'rgba(0, 250, 154, 0.3)',
                  ],
                  borderColor: [
                      'rgba(0, 128, 128, 0.3)',
                  ],
                  borderWidth: 1
              }
              ],
            },
            options: {
              scales: {
                y: {
                    beginAtZero: true
                }
            }
            },
          });
          
        }

        consumir_api();
        setInterval(consumir_api, 60000);
      