function myInstanceof(left, right){
    let proto = Object.getPrototypeOf(left);
    let prototype = right.prototype;
    while(true){
        if(proto === null) return false;
        if(proto === prototype) return true;
        proto = Object.getPrototypeOf(proto);
    
    }
}

let num = new Number(2);
console.log(myInstanceof(num, Number)); 