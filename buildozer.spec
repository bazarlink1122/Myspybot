[app]
title = MySpyBot
package.name = myspybot
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,pyTelegramBotAPI,requests
orientation = portrait
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 25b
android.arch = armeabi-v7a
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
