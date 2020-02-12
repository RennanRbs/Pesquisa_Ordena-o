{\rtf1\ansi\ansicpg1252\cocoartf2511
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red183\green111\blue179;\red23\green23\blue23;\red202\green202\blue202;
\red212\green212\blue212;\red194\green126\blue101;\red70\green137\blue204;\red212\green214\blue154;\red140\green211\blue254;
\red113\green184\blue255;\red167\green197\blue152;\red67\green192\blue160;\red89\green156\blue62;}
{\*\expandedcolortbl;;\cssrgb\c77255\c52549\c75294;\cssrgb\c11765\c11765\c11765;\cssrgb\c83137\c83137\c83137;
\cssrgb\c86275\c86275\c86275;\cssrgb\c80784\c56863\c47059;\cssrgb\c33725\c61176\c83922;\cssrgb\c86275\c86275\c66667;\cssrgb\c61176\c86275\c99608;
\cssrgb\c50980\c77647\c100000;\cssrgb\c70980\c80784\c65882;\cssrgb\c30588\c78824\c69020;\cssrgb\c41569\c66275\c30980;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sl320\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 import\cf4 \strokec4 \'c2\'a0random\
\cf2 \strokec2 import\cf4 \strokec4 \'c2\'a0timeit\
\cf2 \strokec2 import\cf4 \strokec4 \'c2\'a0matplotlib\'c2\'a0\cf2 \strokec2 as\cf4 \strokec4 \'c2\'a0mpl\
\
\
mpl.use\cf5 \strokec5 (\cf6 \strokec6 'Agg'\cf5 \strokec5 )\cf4 \strokec4 \
\
\
\cf2 \strokec2 import\cf4 \strokec4 \'c2\'a0matplotlib.pyplot\'c2\'a0\cf2 \strokec2 as\cf4 \strokec4 \'c2\'a0plt\
\pard\pardeftab720\sl320\partightenfactor0
\cf7 \strokec7 def\cf4 \strokec4 \'c2\'a0\cf8 \strokec8 desenhaGrafico\cf4 \strokec4 (\cf9 \strokec9 x\cf4 \strokec4 ,\cf9 \strokec9 y\cf4 \strokec4 ,\cf9 \strokec9 xl\cf4 \strokec4 \'c2\'a0\cf10 \strokec10 =\cf4 \strokec4 \'c2\'a0\cf6 \strokec6 "Entradas"\cf4 \strokec4 ,\'c2\'a0\cf9 \strokec9 yl\cf4 \strokec4 \'c2\'a0\cf10 \strokec10 =\cf4 \strokec4 \'c2\'a0\cf6 \strokec6 "Sa\'c3\'addas"\cf4 \strokec4 ,\'c2\'a0\cf9 \strokec9 name\cf10 \strokec10 =\cf6 \strokec6 'graph.png'\cf4 \strokec4 )\cf5 \strokec5 :\cf4 \strokec4 \
\'c2\'a0\'c2\'a0\'c2\'a0\'c2\'a0fig\'c2\'a0=\'c2\'a0plt.figure\cf5 \strokec5 (\cf4 \strokec4 figsize=\cf5 \strokec5 (\cf11 \strokec11 10\cf5 \strokec5 ,\cf4 \strokec4 \'c2\'a0\cf11 \strokec11 8\cf5 \strokec5 ))\cf4 \strokec4 \
\'c2\'a0\'c2\'a0\'c2\'a0\'c2\'a0ax\'c2\'a0=\'c2\'a0fig.add_subplot\cf5 \strokec5 (\cf11 \strokec11 111\cf5 \strokec5 )\cf4 \strokec4 \
\'c2\'a0\'c2\'a0\'c2\'a0\'c2\'a0ax.plot\cf5 \strokec5 (\cf4 \strokec4 x\cf5 \strokec5 ,\cf4 \strokec4 y\cf5 \strokec5 ,\cf4 \strokec4 \'c2\'a0label\'c2\'a0=\'c2\'a0\cf6 \strokec6 "Melhor\'c2\'a0Tempo"\cf5 \strokec5 )\cf4 \strokec4 \
\'c2\'a0\'c2\'a0\'c2\'a0\'c2\'a0ax.legend\cf5 \strokec5 (\cf4 \strokec4 bbox_to_anchor=\cf5 \strokec5 (\cf11 \strokec11 1\cf5 \strokec5 ,\cf4 \strokec4 \'c2\'a0\cf11 \strokec11 1\cf5 \strokec5 ),\cf4 \strokec4 bbox_transform=plt.gcf\cf5 \strokec5 ()\cf4 \strokec4 .transFigure\cf5 \strokec5 )\cf4 \strokec4 \
\'c2\'a0\'c2\'a0\'c2\'a0\'c2\'a0plt.ylabel\cf5 \strokec5 (\cf4 \strokec4 yl\cf5 \strokec5 )\cf4 \strokec4 \
\'c2\'a0\'c2\'a0\'c2\'a0\'c2\'a0plt.xlabel\cf5 \strokec5 (\cf4 \strokec4 xl\cf5 \strokec5 )\cf4 \strokec4 \
\'c2\'a0\'c2\'a0\'c2\'a0\'c2\'a0fig.savefig\cf5 \strokec5 (\cf4 \strokec4 name\cf5 \strokec5 )\cf4 \strokec4 \
\
\
EXAMPLE\'c2\'a0=\'c2\'a0\cf5 \strokec5 [\cf11 \strokec11 7\cf5 \strokec5 ,\cf4 \strokec4 \'c2\'a0\cf11 \strokec11 6\cf5 \strokec5 ,\cf4 \strokec4 \'c2\'a0\cf11 \strokec11 5\cf5 \strokec5 ,\cf4 \strokec4 \'c2\'a0\cf11 \strokec11 1\cf5 \strokec5 ,\cf4 \strokec4 \'c2\'a0\cf11 \strokec11 8\cf5 \strokec5 ,\cf4 \strokec4 \'c2\'a0\cf11 \strokec11 9\cf5 \strokec5 ,\cf4 \strokec4 \'c2\'a0\cf11 \strokec11 10\cf5 \strokec5 ]\cf4 \strokec4 \
\
\
\cf7 \strokec7 def\cf4 \strokec4 \'c2\'a0\cf8 \strokec8 selectionsort\cf4 \strokec4 (\cf9 \strokec9 to_sort\cf4 \strokec4 )\cf5 \strokec5 :\cf4 \strokec4 \
\'c2\'a0\'c2\'a0\'c2\'a0\'c2\'a0clone\'c2\'a0=\'c2\'a0to_sort.copy\cf5 \strokec5 ()\cf4 \strokec4 \
\'c2\'a0\'c2\'a0\'c2\'a0\'c2\'a0length\'c2\'a0=\'c2\'a0\cf8 \strokec8 len\cf5 \strokec5 (\cf4 \strokec4 clone\cf5 \strokec5 )\cf4 \strokec4 \
\'c2\'a0\'c2\'a0\'c2\'a0\'c2\'a0\cf2 \strokec2 for\cf4 \strokec4 \'c2\'a0count\cf5 \strokec5 ,\cf4 \strokec4 \'c2\'a0_\'c2\'a0\cf10 \strokec10 in\cf4 \strokec4 \'c2\'a0\cf8 \strokec8 enumerate\cf5 \strokec5 (\cf4 \strokec4 clone\cf5 \strokec5 ):\cf4 \strokec4 \
\'c2\'a0\'c2\'a0\'c2\'a0\'c2\'a0\'c2\'a0\'c2\'a0\'c2\'a0\'c2\'a0pivot\'c2\'a0=\'c2\'a0count\
\'c2\'a0\'c2\'a0\'c2\'a0\'c2\'a0\'c2\'a0\'c2\'a0\'c2\'a0\'c2\'a0\cf2 \strokec2 for\cf4 \strokec4 \'c2\'a0count2\'c2\'a0\cf10 \strokec10 in\cf4 \strokec4 \'c2\'a0\cf8 \strokec8 range\cf5 \strokec5 (\cf4 \strokec4 count+\cf11 \strokec11 1\cf5 \strokec5 ,\cf4 \strokec4 \'c2\'a0length\cf11 \strokec11 -1\cf5 \strokec5 ):\cf4 \strokec4 \
\'c2\'a0\'c2\'a0\'c2\'a0\'c2\'a0\'c2\'a0\'c2\'a0\'c2\'a0\'c2\'a0\'c2\'a0\'c2\'a0\'c2\'a0\'c2\'a0\cf2 \strokec2 if\cf4 \strokec4 \'c2\'a0clone\cf5 \strokec5 [\cf4 \strokec4 count2\cf5 \strokec5 ]\cf4 \strokec4 \'c2\'a0<\'c2\'a0clone\cf5 \strokec5 [\cf4 \strokec4 pivot\cf5 \strokec5 ]:\cf4 \strokec4 \
\'c2\'a0\'c2\'a0\'c2\'a0\'c2\'a0\'c2\'a0\'c2\'a0\'c2\'a0\'c2\'a0\'c2\'a0\'c2\'a0\'c2\'a0\'c2\'a0\'c2\'a0\'c2\'a0\'c2\'a0\'c2\'a0pivot\'c2\'a0=\'c2\'a0count2\
\'c2\'a0\'c2\'a0\'c2\'a0\'c2\'a0\'c2\'a0\'c2\'a0\'c2\'a0\'c2\'a0\cf2 \strokec2 if\cf4 \strokec4 \'c2\'a0clone\cf5 \strokec5 [\cf4 \strokec4 count\cf5 \strokec5 ]\cf4 \strokec4 \'c2\'a0>\'c2\'a0clone\cf5 \strokec5 [\cf4 \strokec4 pivot\cf5 \strokec5 ]:\cf4 \strokec4 \
\'c2\'a0\'c2\'a0\'c2\'a0\'c2\'a0\'c2\'a0\'c2\'a0\'c2\'a0\'c2\'a0\'c2\'a0\'c2\'a0\'c2\'a0\'c2\'a0clone\cf5 \strokec5 [\cf4 \strokec4 count\cf5 \strokec5 ],\cf4 \strokec4 \'c2\'a0clone\cf5 \strokec5 [\cf4 \strokec4 pivot\cf5 \strokec5 ]\cf4 \strokec4 \'c2\'a0=\'c2\'a0clone\cf5 \strokec5 [\cf4 \strokec4 pivot\cf5 \strokec5 ],\cf4 \strokec4 \'c2\'a0clone\cf5 \strokec5 [\cf4 \strokec4 count\cf5 \strokec5 ]\cf4 \strokec4 \
\'c2\'a0\'c2\'a0\'c2\'a0\'c2\'a0\cf2 \strokec2 return\cf4 \strokec4 \'c2\'a0clone\
\
\pard\pardeftab720\sl320\partightenfactor0
\cf8 \strokec8 print\cf5 \strokec5 (\cf4 \strokec4 selectionsort\cf5 \strokec5 (\cf4 \strokec4 EXAMPLE\cf5 \strokec5 ))\cf4 \strokec4 \
\
\pard\pardeftab720\sl320\partightenfactor0
\cf7 \strokec7 def\cf4 \strokec4 \'c2\'a0\cf8 \strokec8 shuffle_random\cf4 \strokec4 (\cf9 \strokec9 n\cf4 \strokec4 )\cf5 \strokec5 :\cf4 \strokec4 \
\'c2\'a0\'c2\'a0\'c2\'a0\'c2\'a0result\'c2\'a0=\'c2\'a0\cf12 \strokec12 list\cf5 \strokec5 (\cf8 \strokec8 range\cf5 \strokec5 (\cf4 \strokec4 n\cf5 \strokec5 ))\cf4 \strokec4 \
\'c2\'a0\'c2\'a0\'c2\'a0\'c2\'a0random.shuffle\cf5 \strokec5 (\cf4 \strokec4 result\cf5 \strokec5 )\cf4 \strokec4 \
\'c2\'a0\'c2\'a0\'c2\'a0\'c2\'a0\cf2 \strokec2 return\cf4 \strokec4 \'c2\'a0result\
\
\
options\'c2\'a0=\'c2\'a0\cf5 \strokec5 [\cf11 \strokec11 1000\cf5 \strokec5 ,\cf4 \strokec4 \'c2\'a0\cf11 \strokec11 10000\cf5 \strokec5 ,\cf4 \strokec4 \'c2\'a0\cf11 \strokec11 30000\cf5 \strokec5 ,\cf4 \strokec4 \'c2\'a0\cf11 \strokec11 60000\cf5 \strokec5 ]\cf4 \strokec4 \
\
\
results_random\'c2\'a0=\'c2\'a0\cf5 \strokec5 []\cf4 \strokec4 \
results_inverse\'c2\'a0=\'c2\'a0\cf5 \strokec5 []\cf4 \strokec4 \
\pard\pardeftab720\sl320\partightenfactor0
\cf2 \strokec2 for\cf4 \strokec4 \'c2\'a0option\'c2\'a0\cf10 \strokec10 in\cf4 \strokec4 \'c2\'a0options\cf5 \strokec5 :\cf4 \strokec4 \
\'c2\'a0\'c2\'a0\'c2\'a0\'c2\'a0tempo\'c2\'a0=\'c2\'a0\'c2\'a0\'c2\'a0timeit.timeit\cf5 \strokec5 (\cf6 \strokec6 "selectionsort(\{\})"\cf4 \strokec4 .\cf8 \strokec8 format\cf5 \strokec5 (\cf4 \strokec4 shuffle_random\cf5 \strokec5 (\cf4 \strokec4 option\cf5 \strokec5 )),\cf4 \strokec4 \'c2\'a0setup=\cf6 \strokec6 "from\'c2\'a0__main__\'c2\'a0import\'c2\'a0selectionsort"\cf5 \strokec5 ,\cf4 \strokec4 number=\cf11 \strokec11 1\cf5 \strokec5 )\cf4 \strokec4 \
\'c2\'a0\'c2\'a0\'c2\'a0\'c2\'a0results_random.append\cf5 \strokec5 (\cf4 \strokec4 tempo\cf5 \strokec5 )\cf4 \strokec4 \
\'c2\'a0\'c2\'a0\'c2\'a0\'c2\'a0tempo\'c2\'a0=\'c2\'a0\'c2\'a0\'c2\'a0timeit.timeit\cf5 \strokec5 (\cf6 \strokec6 "selectionsort(\{\})"\cf4 \strokec4 .\cf8 \strokec8 format\cf5 \strokec5 (\cf12 \strokec12 list\cf5 \strokec5 (\cf8 \strokec8 range\cf5 \strokec5 (\cf4 \strokec4 option\cf5 \strokec5 ))[::\cf11 \strokec11 -1\cf5 \strokec5 ]),\cf4 \strokec4 \'c2\'a0setup=\cf6 \strokec6 "from\'c2\'a0__main__\'c2\'a0import\'c2\'a0selectionsort"\cf5 \strokec5 ,\cf4 \strokec4 number=\cf11 \strokec11 1\cf5 \strokec5 )\cf4 \strokec4 \
\'c2\'a0\'c2\'a0\'c2\'a0\'c2\'a0results_inverse.append\cf5 \strokec5 (\cf4 \strokec4 tempo\cf5 \strokec5 )\cf4 \strokec4 \
\
\pard\pardeftab720\sl320\partightenfactor0
\cf13 \strokec13 #\'c2\'a0desenhaGrafico(options,\'c2\'a0results_random,\'c2\'a0name\'c2\'a0='result_random.png')\cf4 \strokec4 \
\cf13 \strokec13 #\'c2\'a0desenhaGrafico(options,\'c2\'a0results_inverse,\'c2\'a0name='result_inverse.png')\cf4 \strokec4 \
}