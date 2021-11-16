package com.example.docker.controller;

import com.example.docker.domain.Member;
import com.example.docker.repository.MemberRepository;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
public class DataController {

    private MemberRepository memberRepository = MemberRepository.getInstance();

    @PostMapping("/data/save")
    public void addMember(@RequestBody Member member){
        memberRepository.save(member);

        List<Member> all = memberRepository.findAll();
        for (Member member1 : all) {
            System.out.println("member1.getUsername() = " + member1.getUsername());
            System.out.println("member1.getAge() = " + member1.getAge());
            System.out.println("member1.getId() = " + member1.getId());
        }

    }

    @GetMapping("/members")
    public List<Member> listMembers(){
        List<Member> all = memberRepository.findAll();
        return all;
    }
}
