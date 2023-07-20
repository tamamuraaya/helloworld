ver = "0.2"

class Member:
    def __init__(self, name, words=""):
        self.name = name
        self.words = words
    
    def name(self):
        return self.name

print("メンバーリスト・アプリ  Ver. "+ver)
print("--------------------------------")

# メンバー追加
mlist = []
newmember = Member("江頭2:50", "エガちゃんです！")
mlist.append(newmember)

<<<<<<< Updated upstream
<<<<<<< HEAD
### 以下に自分を追加する ###
newmember = Member("房州優樹", "よろしくです！")
mlist.append(newmember)
=======

### 以下に自分を追加する ###
newmember = Member("吉田 羅生", "よろしくです！")
=======
>>>>>>> Stashed changes

### 以下に自分を追加する ###
newmember = Member("玉村　彩", "オーキャン参加します")
mlist.append(newmember)

### 以下に自分を追加する ###
newmember = Member("大河原翔太", "よろしくお願いいたします。")
mlist.append(newmember)

>>>>>>> 901294554bfb4975aa723a8c5df746849f91fc29

# メンバー表示
print("各メンバーから一言")
print()
for member in mlist:
    print(member.name + " ..... " + member.words)
