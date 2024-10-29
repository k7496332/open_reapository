# pythonプログラムのREADME

## 目次
- [ssh接続時におけるplt.showの有効化](#unable_pltshow)
- [powerpointに合わせたfigureの作成](#create_fig_in_cm)
- [画像からgifへの変換](#image2gif)

## ssh接続時におけるplt.show()の有効化 <a name="unable_pltshow"></a>  
``Unable_pltshow.py``   
ssh接続で``plt.show()``を有効にするプログラムです。  
importして関数として使用するか、プロットの前に直接記述することで機能します。

## powerpointに合わせたfigureの作成 <a name="create_fig_in_cm"></a>  
``create_fig_in_cm``  
このプログラムでは、PowerPoint上のサイズ（cm単位）を基に、Matplotlibのfigsizeに適切な値を自動で設定できる関数を提供します。これにより、PowerPointスライドに合わせた図の作成が簡単になり、再調整の手間が省けます。

## 画像からgifへの変換 <a name="image2gif"></a>  
``image2gif.py``  
このプログラムでは、複数の画像からgifを作成することができます。
