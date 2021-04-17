function changeQuantity(action, bookID, cartID){
    // Disable increment/decrement buttons
    lockButtons();
    
    // Extract new quantity
    let quantity = $("#item-" + bookID).val();
    if (action === "increment"){
        quantity++;
    }
    else if (action === "decrement"){
        quantity--;
    }
    else if (action === "remove"){
        quantity = 0;
    }

    // Required for Django POST request
    const csrftoken = Cookies.get('csrftoken');

    function csrfSafeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    // AJAX request
    $.ajax({
        headers: {
            "X-CSRFToken": csrftoken
        },
        url: "/change_quantity",
        type: 'POST',
        data: {
            'book_id': JSON.stringify(bookID),
            'cart_id': JSON.stringify(cartID),
            'quantity': JSON.stringify(quantity) 
        },
        dataType: 'json',
        success: 
            function(response){
                // Refresh page if quantity is 0
                if (response[0] === "refresh"){
                    location.reload();
                }
                else{
                    // Update book quantity
                    const book = response[0]['book'];
                    const quantity = response[0]['quantity'];
                    $("#item-" + book).val(quantity);
                    
                    // Update item total and subtotal
                    const price = $("#item-" + book + "-price").html();  
                    if (action === "decrement"){
                        const newTotal = (parseFloat($("#item-" + book + "-total").html()) - parseFloat(price)).toFixed(2);
                        const newSubtotal = (parseFloat($("#subtotal").html()) - parseFloat(price)).toFixed(2);
                        $("#item-" + book + "-total").html(newTotal);
                        $("#subtotal").html(newSubtotal);
                    }
                    else if (action === "increment"){
                        const newTotal = (parseFloat($("#item-" + book + "-total").html()) + parseFloat(price)).toFixed(2);
                        const newSubtotal = (parseFloat($("#subtotal").html()) + parseFloat(price)).toFixed(2);
                        $("#item-" + book + "-total").html(newTotal);
                        $("#subtotal").html(newSubtotal);
                    }
                
                    // Update cart item count
                    $("#cart-count").html("(" + response[0]['cartCount'] + ")");

                    // Enable increment/decrement buttons
                    unlockButtons();
                }
            },
        error: 
            function() {
                alert("Couldn't remove item");
                unlockButtons();
            } 
    });
}  

function lockButtons(){
    $("#decrement-button").attr("disabled", "true");
    $("#increment-button").attr("disabled", "true");
}

function unlockButtons(){
    $("#decrement-button").attr("disabled", "false");
    $("#increment-button").attr("disabled", "false");
}