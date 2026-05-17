# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_harvest_total.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fgoncal2 <fgoncal2@student.42lisboa.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/08 15:46:57 by fgoncal2          #+#    #+#              #
#    Updated: 2026/01/08 16:25:12 by fgoncal2         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_harvest_total():
	day1 = int(input("Day 1 harvest: "))
	day2 = int(input("Day 2 harvest: "))
	day3 = int(input("Day 3 harvest: "))
	sum = day1 + day2 + day3
	print("Total harvest:", sum)