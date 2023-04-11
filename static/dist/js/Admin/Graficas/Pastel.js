
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
            type: "doughnut",
            data: {
              labels: [
                "Operadores activos",
                "Operadores inactivos",
                "Auxiliares",
              ],
              datasets: [
                {
                  label: "# ",
                  data: [
                    data.operadores_activos,
                    data.operadores_inactivos,
                    data.auxiliares,
                  ],
                  backgroundColor: [
                    "rgba(144, 238, 144)",
                    "rgba(220, 20, 60)",
                    "rgba(32, 178, 170)",
                  ],
                  hoverOffset: 4,
                },
              ],
            },
            options: {},
          });
        }

        consumir_api();
        setInterval(consumir_api, 60000);
      