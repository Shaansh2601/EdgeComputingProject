
    // Initialize Pusher
    var pusher = new Pusher('8ad4d5b94378b706db99', {
        cluster: 'ap2'
    });

    // Subscribe to table channel
    var channel = pusher.subscribe('table');

    channel.bind('new-record', (data) => {

       $('#products').append(`
            <tr id="${data.data.product_id} ">
                <td> ${data.data.sr_no} </td>
                <td> ${data.data.product_id} </td>
                <td> ${data.data.name_of_product} </td>
                <td> ${data.data.quantity} </td>
                <td> ${data.data.cost_of_product} </td>
                <td>${data.data.final_cost_of_product}</td>
            </tr>
       `)
    });

    channel.bind('update-record', (data) => {


         $(`#${data.data.product_id}`).html(`
            <th scope="row"> ${data.data.product_id} </th>
            <td> ${data.data.name_of_product} </td>
            <td> ${data.data.quantity} </td>
            <td> ${data.data.cost_of_product} </td>
        `)
     });
