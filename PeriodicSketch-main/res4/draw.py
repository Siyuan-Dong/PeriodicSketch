#!/usr/bin/env python
# coding=utf-8

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import argparse

def main():
    parser = argparse.ArgumentParser(description="draw results of a single flow")
    parser.add_argument('--k', default="syn", type=str, help='print info of the k_th flow')
    parser.add_argument('--log', default=True, type=bool, help='log x-axis')
    global args
    args = parser.parse_args()


    # est_file_5000 = u'./result/top-' + args.k + u'_est_5000.csv'
    # est_data_5000 = pd.read_csv(est_file_5000)
    # est_file_7000 = u'./result/top-' + args.k + u'_est_7000.csv'
    # est_data_7000 = pd.read_csv(est_file_7000)

    lis = ["AAE","ARE","RR","PR","F1"]
    for i in lis:
        real_file1 = u'./'+'cmp_algo_100000.000000'+'.csv'
        real_data1 = pd.read_csv(real_file1)
        real_file2 = u'./'+'Ours_100000.000000'+'.csv'
        real_data2 = pd.read_csv(real_file2)


        # plt.rc('font', family='SimSun-ExtB')
        # plt.xlim(0,1000000000)
        # plt.xscale('symlog', linthresh=0.000000000000000000001)

        ax = plt.gca()
        plt.rc('font', family='Arial')
        plt.figure(figsize=(5.5, 4.5))
        if i=="AAE" or i=="ARE":
            plt.yscale('log')
        plt.xscale('log',base=2)
        
        plt.tick_params(labelsize = 19)
        # plt.rcParams['font.sans-serif']=['SimHei']
        # plt.rcParams['axes.unicode_minus']=False
        # print(matplotlib.matplotlib_fname())
        # print(matplotlib.get_cachedir())

        plt.xlabel(r'K',fontweight='bold',fontsize=24)#设置x轴，并设定字号大小
        plt.ylabel(i,fontweight='bold',fontsize=24)#设置y轴，并设定字号大小
        # if i=="AAE" or i=="ARE":
            # ax.set_yscale('log')
        # plt.xscale('log')
        # plt.xscale('symlog', linthresh=0.01)


        # ax = plt.gca()

        # if args.log == True:
        #     ax.set_xscale('log')
        # if args.k=="res_tiny":
        #     plt.plot(real_data['memory'], real_data['MAE'], label='tiny', linestyle='-', marker=None, markersize=10, alpha = 1, linewidth=2, markerfacecolor='none', markeredgewidth=2)
        # elif args.k=="tiny_dist":
        plt.plot(real_data1['k'], real_data1[i], label=r"cmp", linestyle='-', marker="^", markersize=10, alpha = 1, linewidth=3, markeredgewidth=2)
        plt.plot(real_data2['k'], real_data2[i], label=r"Ours", linestyle='-', marker="v", markersize=10, alpha = 1, linewidth=3, markeredgewidth=2)
        # plt.plot(real_data3['mem']/1000, real_data3[i], label=r"Baseline", linestyle='-', marker="o", markersize=10, alpha = 1, linewidth=3, markeredgewidth=2)
        
        
        
        
        
        plt.legend(loc = 'best', ncol=1, handlelength=3)
        leg = plt.gca().get_legend() #或leg=ax.get_legend()
        ltext = leg.get_texts()
        plt.setp(ltext,fontweight='bold',fontsize = 20)
        #plt.setp(ltext,fontsize = 22)

        #plt.legend(fontsize = 16)
        plt.grid(True, linestyle='--', axis='y')
        plt.grid(True, linestyle='--', axis='x')
        plt.tight_layout()

        plt.savefig('./'+i+'.pdf')
        plt.show()


if __name__ == "__main__":
    main()
