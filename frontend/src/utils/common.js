export default {
    getContent(html,maxLen=40) {
        html = html.replace(/(^\s*)|(\s*$)/g, "").replace(/<[^<^>]*>/g, "").replace(/[\r\n]/g, "");
        if (html.length > maxLen) {
            html = html.substring(0, maxLen) + '...';
        }
        return html;
    }
}