import os
# rootdir = '/Volumes/workplace/arytonhoi.github.io/blink_code_reviews'
rootdir = './blink_code_reviews'

with open('blink_code_reviews_list.html', 'w') as f:
    f.write('<html lang="en"><body>')
    repos = next(os.walk(rootdir))[1]
    for repo in repos:
        f.write("<li>")
        f.write(repo)
        f.write("<ul>")
        repo_path = "/".join([rootdir, repo])
        reviews = next(os.walk(repo_path))[1]
        for review in reviews:
            f.write("<li>")
            f.write(review)
            f.write("<ul>")
            review_path = "/".join([repo_path, review])
            for file_diff in os.listdir(review_path):
                file_diff_path = "/".join([review_path, file_diff])
                f.write(f'<li><a target="_blank" and rel="noopener noreferrer" href="{file_diff_path}">{file_diff}</a></li>')
            f.write("</ul>")
            f.write("</li>")
        f.write("</ul>")
        f.write("</li>")
    f.write("</body></html>")
            