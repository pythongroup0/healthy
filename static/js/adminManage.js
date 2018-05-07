$( $(".tm-right-column section")[0] ).show().siblings().hide();
$(".tm-nav-item a").on('click',function(){
    if( this.innerHTML=="用户管理" ){
        $( $(".tm-right-column section")[1] ).show().siblings().hide();
    }else if( this.innerHTML=="菜品管理" ){
        $( $(".tm-right-column section")[2] ).show().siblings().hide();
    }else if( this.innerHTML=="食材管理" ){
        $( $(".tm-right-column section")[3] ).show().siblings().hide();
    }else{
        $( $(".tm-right-column section")[4] ).show().siblings().hide();
    }
})
//按钮添加功能的script代码
$('#exampleModal').on('show.bs.modal', function (event) {

})
//分页
init();
re_init();
function init(){
    $(".tm-nav-item a").on('click',function(){
        if( this.innerHTML=="用户管理" ){
            $( $(".tm-right-column section")[1] ).show().siblings().hide();
        }else if( this.innerHTML=="菜品管理" ){
            $( $(".tm-right-column section")[2] ).show().siblings().hide();
        }else if( this.innerHTML=="食材管理" ){
            $( $(".tm-right-column section")[3] ).show().siblings().hide();
        }else{
            $( $(".tm-right-column section")[4] ).show().siblings().hide();
        }
    });
}
function re_init(){
    var show_page = $("#show_page").val();
    if(show_page == ""){
        $( $(".tm-right-column section")[0] ).show().siblings().hide();
    }else if( show_page == "user"){
        $( $(".tm-right-column section")[1] ).show().siblings().hide();
    }else if( show_page=="dish" ){
        $( $(".tm-right-column section")[2] ).show().siblings().hide();
    }else if( show_page=="ingredients" ){
        $( $(".tm-right-column section")[3] ).show().siblings().hide();
    }
}