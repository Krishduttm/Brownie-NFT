# Brownie-NFT

There are two sections in this project - 

A) Simple Collectible - This is a basic implementation of nft minting using the erc721 from open zeppelin. There is also a deploy script which deploys this. The token uri was directly provided from an already existing ipfs json file.

B)Advanced collectible - In this implementation , i used three pictures of dogs and use the chailink vrf contract to randomly select a dog to mint as an nft. Then I also wrote a script to create a metadata for the nft and also set the token uri. Lastly, i wrote a script to upload this metadata to ipfs and used the pinata website to upload the dog picture and make sure it stays online always even when the ipfs node fails. When all the scripts are run, we can check that our nft will be present in our address and can be viewed on testnet opensea. 

I have also typed unit and integration tests for both the sections to make sure they worked fine

In this prohect i learnt about how nft's work, erc721, open sea, ipfs , increased my experience in writing tests , working with smart contracts and brownie.
