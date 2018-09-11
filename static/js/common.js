/**
 * Created by tarena on 18-9-3.
 */
function createxhr() {
    if(window.XMLHttpRequest){
        return new XMLHttpRequest()
    }else{
        return new ActiveXObject('Microsoft.XMLHTTP')
    }
}