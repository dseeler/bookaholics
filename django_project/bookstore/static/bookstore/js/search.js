window.onload = (event) => {
    $("#genre-option").remove(0);
}

function reset(){
    location.reload();
}

// Ajax filter request
function filter(){
    const genre = $("input[name='genre']:checked").val();
    const price_range = $("input[name='price-range']:checked").val();
    const rating = $("input[name='rating']:checked").val();

    
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
         url: "/filter_search",
         type: 'POST',
         data: {
             'genre': JSON.stringify(genre),
             'price_range': JSON.stringify(price_range),
             'rating': JSON.stringify(rating) 
         },
         dataType: 'json',
         success: 
             function(response){

                // Extract json book data
                const books = response[0];           
    
                // Change results header if no results were found
                const num_results = Object.keys(books).length;
                if (num_results !== 0){
                    $("#content-right-title").html(num_results + " result(s) found");
                }
                else{
                    $("#content-right-title").html("No books found");
                }

                // Add book results to HTML content
                let results = "";
                for (let book in books){
                    results += "<div id='book-container'>";
                    results += "<a href='book_detail/" + formatTitle(books[book]['title']) + "/'>";
                    results += "<img src='" + books[book]['image'] + "' id='book-image'>";  
                    results += "<p id='book-title'>" + books[book]['title'] + "</p>";
                    results += "<p id='book-author'>" + books[book]['author'] + "</p>";
                    results += "<span id='book-rating-" + books[book]['rating'] + "'>" + getRatingStars(books[book]['rating']) + "</span>";
                    results += "<p id='book-price'><b>$" + books[book]['price'] + "</b></p>";
                    results += "</a>";
                    results += "</div>"; 
                }
                $("#search-results").html(results);
             },
         error: 
             function() {
                 alert("Something went wrong");
             } 
     });
     
}

function getRatingStars(rating){
    let stars = "";
    for (let i = 0; i < 5; i++){
        if (i < rating){
            stars += "<span class='fa fa-star checked'></span>";
        }
        else{
            stars += "<span class='fa fa-star'></span>";
        }
    }
    return stars;
}

function formatTitle(title){
    return title.replaceAll("'", "\'");
}