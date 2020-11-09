var updateBtns = document.getElementsByClassName('update-cart')

for(var i=0; i < updateBtns.length; i++)
{
    updateBtns[i].addEventListener('click',function()
    {
        var productId = this.dataset.product
        var userid = this.dataset.userid
        var action = this.dataset.action
        console.log('productId:',productId,'action:',action)

        console.log('user:',user)
        if(user == 'AnonymousUser')
        {
            console.log("Not logged in")
        }
        else
        {
            updateUserOrder(productId, action,userid)
        }
    })
}

function updateUserOrder(productId,action,userid)
{
    console.log('User is logged in, sending data')

    var url = '/update_item/'

    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFTOKEN':csrftoken,
        },
        body:JSON.stringify({'productId': productId,'action':action,'userid':userid})
    })

    .then((response) => {
        return response.json()
    })
    .then((data)=>{
        console.log('Data:',data)
        location.reload()
    })
}