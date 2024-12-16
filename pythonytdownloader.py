import yt_dlp

def downloader(url):
    ydl_opts = {
        'format ' : 'bestvideo[height<=480]',
        'noplaylist':True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


if __name__ == "__main__":
    vurl=input("Enter the youtube url :  ")


downloader(vurl)


#first install the pip ;; pip install yt-dlp
#enter the link after running 

#this video will be saved into your files
#note it also have sound it will be glitched in vs code sometimes but you can be able to view it on your folders section(raza)



"""YOU CAN TRY THIS LINK 
    https://youtu.be/llGQMlkgkpk?feature=shared   """