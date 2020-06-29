var m, n;
        m = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/",
        n = {
            rotl: function(e, t) {
                return e << t | e >>> 32 - t
            },
            rotr: function(e, t) {
                return e << 32 - t | e >>> t
            },
            endian: function(e) {
                if (e.constructor == Number)
                    return 16711935 & n.rotl(e, 8) | 4278255360 & n.rotl(e, 24);
                for (var t = 0; t < e.length; t++)
                    e[t] = n.endian(e[t]);
                return e
            },
            randomBytes: function(e) {
                for (var t = []; e > 0; e--)
                    t.push(Math.floor(256 * Math.random()));
                return t
            },
            bytesToWords: function(e) {
                for (var t = [], s = 0, o = 0; s < e.length; s++,
                o += 8)
                    t[o >>> 5] |= e[s] << 24 - o % 32;
                return t
            },
            wordsToBytes: function(e) {
                for (var t = [], s = 0; s < 32 * e.length; s += 8)
                    t.push(e[s >>> 5] >>> 24 - s % 32 & 255);
                return t
            },
            bytesToHex: function(e) {
                for (var t = [], s = 0; s < e.length; s++)
                    t.push((e[s] >>> 4).toString(16)),
                    t.push((15 & e[s]).toString(16));
                return t.join("")
            },
            hexToBytes: function(e) {
                for (var t = [], s = 0; s < e.length; s += 2)
                    t.push(parseInt(e.substr(s, 2), 16));
                return t
            },
            bytesToBase64: function(e) {
                for (var t = [], s = 0; s < e.length; s += 3)
                    for (var n = e[s] << 16 | e[s + 1] << 8 | e[s + 2], r = 0; r < 4; r++)
                        8 * s + 6 * r <= 8 * e.length ? t.push(o.charAt(n >>> 6 * (3 - r) & 63)) : t.push("=");
                return t.join("")
            },
            base64ToBytes: function(e) {
                e = e.replace(/[^A-Z0-9+\/]/gi, "");
                for (var t = [], s = 0, n = 0; s < e.length; n = ++s % 4)
                    0 != n && t.push((o.indexOf(e.charAt(s - 1)) & Math.pow(2, -2 * n + 8) - 1) << 2 * n | o.indexOf(e.charAt(s)) >>> 6 - 2 * n);
                return t
            }
        }

function _ff(e, t, s, o, n, r, i) {
            var a = e + (t & s | ~t & o) + (n >>> 0) + i;
            return (a << r | a >>> 32 - r) + t
        }
      
function _gg(e, t, s, o, n, r, i) {
            var a = e + (t & o | s & ~o) + (n >>> 0) + i;
            return (a << r | a >>> 32 - r) + t
        }

function _hh(e, t, s, o, n, r, i) {
            var a = e + (t ^ s ^ o) + (n >>> 0) + i;
            return (a << r | a >>> 32 - r) + t
        }

function _ii(e, t, s, o, n, r, i) {
            var a = e + (s ^ (t | ~o)) + (n >>> 0) + i;
            return (a << r | a >>> 32 - r) + t
        }
var o = {
            utf8: {
                stringToBytes: function(e) {
                    return o.bin.stringToBytes(unescape(encodeURIComponent(e)))
                },
                bytesToString: function(e) {
                    return decodeURIComponent(escape(o.bin.bytesToString(e)))
                }
            },
            bin: {
                stringToBytes: function(e) {
                    for (var t = [], s = 0; s < e.length; s++)
                        t.push(255 & e.charCodeAt(s));
                    return t
                },
                bytesToString: function(e) {
                    for (var t = [], s = 0; s < e.length; s++)
                        t.push(String.fromCharCode(e[s]));
                    return t.join("")
                }
            }
        };
function bytesToWords(e) {
                for (var t = [], s = 0, o = 0; s < e.length; s++,
                o += 8)
                    t[o >>> 5] |= e[s] << 24 - o % 32;
                return t
            }

function a(t, s) {
            t = o.bin.stringToBytes(t)
            for (var a = bytesToWords(t), d = 8 * t.length, l = 1732584193, u = -271733879, c = -1732584194, m = 271733878, p = 0; p < a.length; p++)
                a[p] = 16711935 & (a[p] << 8 | a[p] >>> 24) | 4278255360 & (a[p] << 24 | a[p] >>> 8);
            a[d >>> 5] |= 128 << d % 32,
            a[14 + (d + 64 >>> 9 << 4)] = d;
            var f = _ff
              , h = _gg
              , g = _hh
              , v = _ii;
            for (p = 0; p < a.length; p += 16) {
                var j = l
                  , b = u
                  , _ = c
                  , y = m;
                l = f(l, u, c, m, a[p + 0], 7, -680876936),
                m = f(m, l, u, c, a[p + 1], 12, -389564586),
                c = f(c, m, l, u, a[p + 2], 17, 606105819),
                u = f(u, c, m, l, a[p + 3], 22, -1044525330),
                l = f(l, u, c, m, a[p + 4], 7, -176418897),
                m = f(m, l, u, c, a[p + 5], 12, 1200080426),
                c = f(c, m, l, u, a[p + 6], 17, -1473231341),
                u = f(u, c, m, l, a[p + 7], 22, -45705983),
                l = f(l, u, c, m, a[p + 8], 7, 1770035416),
                m = f(m, l, u, c, a[p + 9], 12, -1958414417),
                c = f(c, m, l, u, a[p + 10], 17, -42063),
                u = f(u, c, m, l, a[p + 11], 22, -1990404162),
                l = f(l, u, c, m, a[p + 12], 7, 1804603682),
                m = f(m, l, u, c, a[p + 13], 12, -40341101),
                c = f(c, m, l, u, a[p + 14], 17, -1502002290),
                l = h(l, u = f(u, c, m, l, a[p + 15], 22, 1236535329), c, m, a[p + 1], 5, -165796510),
                m = h(m, l, u, c, a[p + 6], 9, -1069501632),
                c = h(c, m, l, u, a[p + 11], 14, 643717713),
                u = h(u, c, m, l, a[p + 0], 20, -373897302),
                l = h(l, u, c, m, a[p + 5], 5, -701558691),
                m = h(m, l, u, c, a[p + 10], 9, 38016083),
                c = h(c, m, l, u, a[p + 15], 14, -660478335),
                u = h(u, c, m, l, a[p + 4], 20, -405537848),
                l = h(l, u, c, m, a[p + 9], 5, 568446438),
                m = h(m, l, u, c, a[p + 14], 9, -1019803690),
                c = h(c, m, l, u, a[p + 3], 14, -187363961),
                u = h(u, c, m, l, a[p + 8], 20, 1163531501),
                l = h(l, u, c, m, a[p + 13], 5, -1444681467),
                m = h(m, l, u, c, a[p + 2], 9, -51403784),
                c = h(c, m, l, u, a[p + 7], 14, 1735328473),
                l = g(l, u = h(u, c, m, l, a[p + 12], 20, -1926607734), c, m, a[p + 5], 4, -378558),
                m = g(m, l, u, c, a[p + 8], 11, -2022574463),
                c = g(c, m, l, u, a[p + 11], 16, 1839030562),
                u = g(u, c, m, l, a[p + 14], 23, -35309556),
                l = g(l, u, c, m, a[p + 1], 4, -1530992060),
                m = g(m, l, u, c, a[p + 4], 11, 1272893353),
                c = g(c, m, l, u, a[p + 7], 16, -155497632),
                u = g(u, c, m, l, a[p + 10], 23, -1094730640),
                l = g(l, u, c, m, a[p + 13], 4, 681279174),
                m = g(m, l, u, c, a[p + 0], 11, -358537222),
                c = g(c, m, l, u, a[p + 3], 16, -722521979),
                u = g(u, c, m, l, a[p + 6], 23, 76029189),
                l = g(l, u, c, m, a[p + 9], 4, -640364487),
                m = g(m, l, u, c, a[p + 12], 11, -421815835),
                c = g(c, m, l, u, a[p + 15], 16, 530742520),
                l = v(l, u = g(u, c, m, l, a[p + 2], 23, -995338651), c, m, a[p + 0], 6, -198630844),
                m = v(m, l, u, c, a[p + 7], 10, 1126891415),
                c = v(c, m, l, u, a[p + 14], 15, -1416354905),
                u = v(u, c, m, l, a[p + 5], 21, -57434055),
                l = v(l, u, c, m, a[p + 12], 6, 1700485571),
                m = v(m, l, u, c, a[p + 3], 10, -1894986606),
                c = v(c, m, l, u, a[p + 10], 15, -1051523),
                u = v(u, c, m, l, a[p + 1], 21, -2054922799),
                l = v(l, u, c, m, a[p + 8], 6, 1873313359),
                m = v(m, l, u, c, a[p + 15], 10, -30611744),
                c = v(c, m, l, u, a[p + 6], 15, -1560198380),
                u = v(u, c, m, l, a[p + 13], 21, 1309151649),
                l = v(l, u, c, m, a[p + 4], 6, -145523070),
                m = v(m, l, u, c, a[p + 11], 10, -1120210379),
                c = v(c, m, l, u, a[p + 2], 15, 718787259),
                u = v(u, c, m, l, a[p + 9], 21, -343485551),
                l = l + j >>> 0,
                u = u + b >>> 0,
                c = c + _ >>> 0,
                m = m + y >>> 0
            }
            return n.endian([l, u, c, m])
        }


function wordsToBytes(e) {
   for (var t = [], s = 0; s < 32 * e.length; s += 8)
       t.push(e[s >>> 5] >>> 24 - s % 32 & 255);
   return t
}

function bytesToHex(e) {
    for (var t = [], s = 0; s < e.length; s++)
        t.push((e[s] >>> 4).toString(16)),
        t.push((15 & e[s]).toString(16));
    return t.join("")
}



function getpwd(pwd){
  res = a(pwd)
  var s = wordsToBytes(res);
  return bytesToHex(s)

}
