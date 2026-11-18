公開後の初回匿名照合は、Git Treesへcommit IDを渡したとき応答shaもそのcommit IDになる挙動を、実tree IDと誤って比較して停止した。公開操作とファイル内容の失敗ではない。Git commit APIでtree参照を先に照合し、そのtree IDをGit Trees APIへ渡す形に直した。再公開・再コミットは行わない。
