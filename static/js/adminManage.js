// 左右侧分栏
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
//点击弹出框
$('#exampleModal').on('show.bs.modal', function (event) {

        })
