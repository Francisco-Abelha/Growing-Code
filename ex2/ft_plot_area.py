# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plot_area.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fgoncal2 <fgoncal2@student.42lisboa.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/08 15:31:43 by fgoncal2          #+#    #+#              #
#    Updated: 2026/01/08 16:25:37 by fgoncal2         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plot_area():
	length = int(input("Enter length: "))
	width = int(input("Enter width: "))
	area = length * width
	print("Plot area:", area)
