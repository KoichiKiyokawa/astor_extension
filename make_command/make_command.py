import subprocess
import sys

# 環境によって変わる定数
BUG_SRC_LOCATION = '/home/kiyokawa/defects4j/tmp/'
# BUG_SRC_LOCATION = '/Users/koichi/autoBugRepair/defects4j/tmp/'

# 修正対象の名前を入力
# ex) chart_1
src_bug_id = sys.argv[1]

try:
    srcjavafolder = subprocess.check_output('defects4j export -p dir.src.classes -w {}'.format(BUG_SRC_LOCATION+src_bug_id).split()).decode()
    srctestfolder = subprocess.check_output('defects4j export -p dir.src.tests -w {}'.format(BUG_SRC_LOCATION+src_bug_id).split()).decode()
    binjavafolder = subprocess.check_output('defects4j export -p dir.bin.classes -w {}'.format(BUG_SRC_LOCATION+src_bug_id).split()).decode()
    bintestfolder = subprocess.check_output('defects4j export -p cp.test -w {}'.format(BUG_SRC_LOCATION+src_bug_id).split()).decode()
    dependencies = subprocess.check_output('defects4j export -p cp.test -w {}'.format(BUG_SRC_LOCATION+src_bug_id).split()).decode()
except:
    raise ValueError('引数のうちいずれかが取得できませんでした')

print('bintestfolderを指定する必要があります')
print(bintestfolder)
print(' : ', end='')
bintestfolder = input()

print('↓これをコピペすればOK')
print('\
java -cp $(cat /tmp/astor-classpath.txt):target/classes fr.inria.main.evolution.AstorMain \
-srcjavafolder {} \
-srctestfolder {} \
-binjavafolder {} \
-bintestfolder {} \
-dependencies {} \
-jvm4testexecution /usr/lib/jvm/java-1.7.0-openjdk-1.7.0.191-2.6.15.4.el7_5.x86_64/jre/bin/ \
-location {}\
'
.format(
    srcjavafolder,
    srctestfolder,
    binjavafolder,
    bintestfolder,
    dependencies,
    BUG_SRC_LOCATION + src_bug_id
)
)
