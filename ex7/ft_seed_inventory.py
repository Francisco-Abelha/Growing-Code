# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_seed_inventory.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fgoncal2 <fgoncal2@student.42lisboa.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/08 16:38:40 by fgoncal2          #+#    #+#              #
#    Updated: 2026/01/08 16:54:33 by fgoncal2         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_seed_inventory(seed_type: str, quantity: int, unit: str):
	if unit == "packets":
		print(f"{seed_type.capitalize()} seeds: {quantity} packets available")
	elif unit == "grams":
		print(f"{seed_type.capitalize()} seeds: {quantity} grams total")
	elif unit == "area":
		print(f"{seed_type.capitalize()} seeds: covers {quantity} square meters")
	else:
		print("Unknown unit type")
