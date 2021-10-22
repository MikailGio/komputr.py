console.log("test") ;

// variable
var nama = "Mikail" ;
var umur = 15;
var lakilaki = true
if (lakilaki) {
    console.log("saya perempuan");
} else {
    console.log("saya laki-laki");
}

var daftarNama = [
    "Mikail",
    "Giovanni",
    "Mofsol",
]

var panjang = daftarNama.length
daftarNama.push("tambahan")

console.log(daftarNama[3])

// 1. loop variable
// 2. end value / syarat perulangan
// 3. loop operation
for (var i = 0; i < 5; i++) {
    console.log(i + " loop")
}

var i = 0;
while (i < 5) {
    console.log(i + " loop2");
    i++
}

var j = 5
var loop = true
while (loop) {
    j--;
    console.log(loop + " "+ j + " loop3");
    if (j < 0) {
        loop = false;
    }
}

// kesalahan dalam membuat suatu perulangan
// infinite loop
// untuk mengubah suatu loop agar dia jadi valid
// maka loop variable harus dibandngkan dengan syarat perulangannya
// jika bisa true maka loop minimal jalasn sekali
// apakah loop variable mendekatkati syarat perulangan atau menjauhi 
// apabila menjauhi maka akan terjadi infinite loop, dan harus diubah

// FUNCTION
function tambah(a, b) {
    return a+b;
}

// VARIABLE
// 1. declaration & assingment
var hasil =  tambah(1, 3)
console.log(hasil);
// 2. assingment
hasil = tambah(2, 5);
console.log(hasil);

var kali = function(a, b){
    return a*b;
}

// 3. declaration only
var hasil2
hasil2 = kali(2, 5);
console.log(hasil2);

hasil2 = kali(3,6)
console.log(hasil2);

// loop luar 1 
// i = 0
// false
// hasil *

// loop luar 2
// i = 1
// j = 0; true; star = "**"
// j = 1; false
// hasil **

// loop luar 3
// i = 2;
// j = 0; true; star = "**"
// j = 1; true; star = "***"
// j = 2; false
// hasil ***

// dst
for (var i = 0; i < 5; i++) {
    var star = "*";
    for(var j = 0; j < i; j++) {
        star = star + "*";
    }
    console.log(star);
}

// *****
// ****
// ***
// **
// *

for(var i = 5; i > 0; i--) {
    var star = "";
    for(var j = 0; j > i; j--) {
        star = star - "*" ;
    }
    console.log(star);
}
