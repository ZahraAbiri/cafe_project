  $(document).ready(function () {
        // Activate tooltip
        $('[data-toggle="tooltip"]').tooltip();

        // Select/Deselect checkboxes
        var checkbox = $('table tbody input[type="checkbox"]');
        $("#selectAll").click(function () {
            if (this.checked) {
                checkbox.each(function () {
                    this.checked = true;
                });
            } else {
                checkbox.each(function () {
                    this.checked = false;
                });
            }
        });
        checkbox.click(function () {
            if (!this.checked) {
                $("#selectAll").prop("checked", false);
            }
        });

        // console.log( JSON.stringify(che))
    });

    //
    // $("#myTable").on('click', '.btnSelect', function () {
    //     var currentRow = $(this).closest("tr");
    //     console.log('lll55555lll')
    //     var col2 = currentRow.find("td:eq(1)").text();
    //     let data = {
    //         id: col2
    //     }
    //     axios.post("http://localhost:5000/delete_menu_item", data).then((res) => {
    //         res.data
    //     })
    //     var col3;
    // })
    // $("#myTable").on('click', '.btnSelects', function () {
    //     var currentRow = $(this).closest("tr");
    //     col3 = currentRow.find("td:eq(1)").text();
    //     console.log(col3)
    // })
    //
    // function MenuUpdate() {
    //
    //     let data = {
    //         id: col3,
    //         name: document.getElementById('nameu').value,
    //         price: document.getElementById('priceu').value,
    //         description: document.getElementById('descriptionu').value
    //     }
    //
    //     console.log(data.description)
    //     axios.post("http://localhost:5000/update_menu_item", data).then((res) => {
    //         res.data
    //     })
    // }
