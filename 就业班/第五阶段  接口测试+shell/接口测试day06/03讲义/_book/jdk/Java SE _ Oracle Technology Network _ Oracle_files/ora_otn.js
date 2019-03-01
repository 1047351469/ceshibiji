/*! ORA_OTN.JS - BUILD: 15th September 2017 v1.30 */
try{oracle.truste.api.getConsentDecision().consentDecision;oracle.truste.api.getConsentDecision().source;}catch(err){var oracle=oracle||{};oracle.truste={};oracle.truste.api={};(function(){var trusteCookieName="notice_preferences";var trusteStorageItemName="truste.eu.cookie.notice_preferences";this.getCookieName=function(){return trusteCookieName;};this.getStorageItemName=function(){return trusteStorageItemName;};}).apply(oracle.truste);(function(){var trusteCommon=oracle.truste;function getCookie(cookieKey){var name=cookieKey+"=";var cookieArray=document.cookie.split(";");for(var i=0;i<cookieArray.length;i++){var c=cookieArray[i];while(c.charAt(0)==" "){c=c.substring(1);}if(c.indexOf(name)==0){return c.substring(name.length,c.length);}}return null;}function getLocalStorageItem(storageKey){if(typeof(Storage)!=="undefined"){return localStorage.getItem(storageKey);}return null;}function getTRUSTeLocalStorageValue(storageKey){var value=getLocalStorageItem(storageKey);if(value!=null){var obj=JSON.parse(value);return obj.value;}return null;}this.getConsentCode=function(){var value=getTRUSTeLocalStorageValue(trusteCommon.getStorageItemName())||getCookie(trusteCommon.getCookieName());if(value==null){return -1;}else{return parseInt(value)+1;}};this.getConsentDecision=function(){var value=this.getConsentCode();if(value==-1){var text='{"consentDecision": 0, "source": "implied"}';return JSON.parse(text);}else{var text='{"consentDecision": '+parseInt(value)+', "source": "asserted"}';return JSON.parse(text);}};}).apply(oracle.truste.api);}var ora_local="ora_code_otn.js";var ora_global="ora_code.js";var elq_global="elqCfg.min.js";var TRUSTeLevel=s_setConsentLevel(0);var ora_path="/us/assets/metrics/";var elq_path="/i/";var _elqQ=_elqQ||[];var isTest=(location.host.indexOf("-stage")!=-1||location.host.indexOf("-content")!=-1||location.host.indexOf("localhost")!=-1||location.host.indexOf("-dev")!=-1);var ora_root=(isTest==true)?"://www-portal-stage.oracle.com":"://www.oracleimg.com";var elq_root="//img03.en25.com";var elq_prodID="1973398186";var elq_devID="30554202";var host_type=(window.location.protocol.toLowerCase().indexOf("https")!=-1)?"https":"http";
/*! Eloqua Tag */
if(!isTest&&TRUSTeLevel!=1){_elqQ.push(["elqSetSiteId",elq_prodID]);_elqQ.push(["elqUseFirstPartyCookie","go.oracle.com"]);_elqQ.push(["elqTrackPageView"]);(function(){function async_load(){var s=document.createElement("script");s.type="text/javascript";s.async=true;s.src=elq_root+elq_path+elq_global;var x=document.getElementsByTagName("script")[0];x.parentNode.insertBefore(s,x);}if(window.addEventListener){window.addEventListener("DOMContentLoaded",async_load,false);}else{if(window.attachEvent){window.attachEvent("onload",async_load);}}})();
/*! Site Catalyst Tag */
}if(TRUSTeLevel!=1){document.write("<script type='text/javascript' src='"+host_type+ora_root+ora_path+ora_local+"'><\/script>");document.write("<script type='text/javascript' src='"+host_type+ora_root+ora_path+ora_global+"'><\/script>");
/*! Additional Tags */
}if((TRUSTeLevel==3||TRUSTeLevel==0)&&location.href.indexOf("/ru/")==-1){document.write("<img src='//20754664p.rfihub.com/ca.html?rb=26998&ca=20754664&_o=26998&_t=20754664&ra=%n' height=0 width=0 style='display:none' alt='Rocket Fuel'/>");ora_bk_version="bkIn:"+ora_local.substr(0,ora_local.indexOf("."))+":v1.3:SentTo"+((isTest)?26595:25867);window.bk_async=function(){var bkTagID=(isTest)?26595:25867;bk_addPageCtx("contTop",(typeof(contTop)!=="undefined")?contTop:"");bk_addPageCtx("contLang",(typeof(language_value)!=="undefined")?language_value:"");bk_addPageCtx("prodInt",(typeof(prodInt)!=="undefined")?prodInt:"");bk_addPageCtx("pgname",(typeof(bk_pgname)!=="undefined")?bk_pgname:"");bk_allow_multiple_calls=true;BKTAG.doTag(bkTagID,1);};(function(){var bk_scripts=document.getElementsByTagName("script")[0];var bk_s=document.createElement("script");bk_s.async=true;bk_s.src="//tags.bkrtx.com/js/bk-coretag.js";bk_scripts.parentNode.insertBefore(bk_s,bk_scripts);}());}function s_setConsentLevel(cLevel){try{cLevel=truste.cma.callApi("getConsentDecision","oracle.com").consentDecision;}catch(err){cLevel=s_getCookieData("notice_preferences").split(":")[0];if(cLevel==""){cLevel=0;}else{cLevel=++cLevel;}}return cLevel;}function s_getCookieData(label){var labelLen=label.length;var cLen=document.cookie.length;var i=0;var cEnd;while(i<cLen){var j=i+labelLen;if(document.cookie.substring(i,j)==label){cEnd=document.cookie.indexOf(";",j);if(cEnd==-1){cEnd=document.cookie.length;}j++;return decodeURIComponent(document.cookie.substring(j,cEnd).replace("+","%20"));}i++;}return"";}