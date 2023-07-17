function adBlockCheck() {
    setTimeout(function() {
        document.body.innerHTML += `<div class="adsbygoogle" id="test-ad"></div>`;
        const testAd = document.getElementById('test-ad');
        const testAdStyle = getComputedStyle(testAd);

        if (testAdStyle.display === 'none') {	
            const banner = document.createElement('div');
            banner.innerHTML = `
            <h3>Ad blocker detected</h3>
            <p>To keep our services free, we use advertising on this site. Please consider supporting us by disabling your ad blocker.</p>
            `
            banner.setAttribute('class', 'alert');
            banner.style = "background: red; color: whitesmoke; width: 100%; padding: 0.8rem; font-size: 1.2rem";
            document.body.prepend(banner);
        } else {
            console.log("Thank you!");
        } 
    },1000)
}

adBlockCheck()
